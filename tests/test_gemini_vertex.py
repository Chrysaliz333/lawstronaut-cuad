#!/usr/bin/env python3
"""
Gemini Test with Vertex AI Google Search Grounding
Tests Gemini's ability to provide precise legal analysis with real-time search using Vertex AI
"""

import os
import json
import time
from datetime import datetime
from pathlib import Path
import sys

# Load .env file manually
env_file = Path(__file__).parent.parent / '.env'  # Look in project root
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value

# Add tests directory to path
sys.path.insert(0, str(Path(__file__).parent))
from test_llm_apis import LawstronautTester

try:
    from google import genai
    from google.genai.types import (
        GenerateContentConfig,
        GoogleSearch,
        HttpOptions,
        Tool,
    )
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("Error: google-genai package not installed")
    print("Install with: pip install --upgrade google-genai")
    sys.exit(1)


class GeminiVertexTester(LawstronautTester):
    """Test Gemini with Vertex AI Google Search grounding for legal research."""

    def __init__(self, project_id=None, location="us-central1"):
        super().__init__(openai_key=None, anthropic_key=None)

        # Set up Vertex AI environment
        self.project_id = project_id or os.getenv('GOOGLE_CLOUD_PROJECT')
        self.location = location or os.getenv('GOOGLE_CLOUD_LOCATION', 'us-central1')

        if not self.project_id:
            print("Error: GOOGLE_CLOUD_PROJECT not set")
            print("Set it in .env file or via environment variable")
            self.client = None
            return

        # Set environment variables for Vertex AI
        os.environ['GOOGLE_CLOUD_PROJECT'] = self.project_id
        os.environ['GOOGLE_CLOUD_LOCATION'] = self.location
        os.environ['GOOGLE_GENAI_USE_VERTEXAI'] = 'True'

        if GEMINI_AVAILABLE:
            try:
                # Create Vertex AI client with search grounding
                self.client = genai.Client(
                    http_options=HttpOptions(api_version="v1")
                )
                self.model_name = 'gemini-2.0-flash-exp'

                # Create Google Search tool
                self.search_tool = Tool(google_search=GoogleSearch())

                print(f"✓ Vertex AI initialized: Project={self.project_id}, Location={self.location}")
            except Exception as e:
                print(f"✗ Error initializing Vertex AI: {e}")
                print("\nMake sure you've authenticated with:")
                print("  gcloud auth application-default login")
                self.client = None
        else:
            self.client = None

    def query_gemini(self, contract_text: str, question: str) -> dict:
        """Query Gemini with Google Search grounding for legal analysis."""
        if not self.client:
            return {
                "error": "Gemini Vertex AI not available",
                "answer": None,
                "model": "gemini-2.0-flash-exp"
            }

        try:
            start_time = time.time()

            system_instruction = """You are a legal research AI assistant with real-time Google Search capabilities.

Your task is to provide precise, well-cited legal analysis. You MUST:

1. **Find the current, applicable law** - Use Google Search to locate the exact regulations, statutes, and case law that apply as of November 5, 2025

2. **Provide pinpoint citations** - Cite specific provisions with precise article/section/paragraph numbers (e.g., "GDPR Article 9(2)(a)", "16 CFR § 910.2(a)(1)", "Cal. Civ. Code § 1798.140(ag)(1)")

3. **Include direct quotes** - For EACH key legal requirement, provide a direct quote from the actual legal text (not summaries or paraphrases)

4. **Link to primary sources** - Provide URLs to official government sites, legislation databases, or authoritative regulatory sources

5. **Apply law to contract** - Analyze specific contract provisions against the legal requirements, citing exact contract section numbers

Your answers should demonstrate:
- Precision in legal citations
- Direct quotes from legislation/regulations
- Correct identification of applicable law
- Clear application to the contract provisions"""

            prompt = f"""FULL CONTRACT TEXT:
{contract_text}

QUESTION:
{question}

CRITICAL REQUIREMENTS:

1. **CURRENT LAW (as of November 5, 2025):**
   - Use Google Search to find the most current version of applicable regulations
   - Verify effective dates and recent amendments
   - If regulations changed in 2024 or 2025, note this explicitly

2. **PINPOINT CITATIONS:**
   - Every legal requirement must have a precise citation
   - Format: Regulation name + Article/Section + Subsection
   - Example: "Regulation (EU) 2024/1689, Article 10(2)(b)"

3. **DIRECT QUOTES:**
   - For EACH key regulation cited, include the actual text in quotation marks
   - Quote the specific provision that establishes the requirement
   - Do not paraphrase - use the exact legal language

4. **PRIMARY SOURCE URLS:**
   - Link to official sources: eur-lex.europa.eu, ecfr.gov, leginfo.legislature.ca.gov, legislation.gov.uk
   - Each major regulation should have at least one primary source URL

5. **CONTRACT APPLICATION:**
   - Reference specific contract sections by number
   - Explain whether each provision complies, partially complies, or fails to comply
   - Identify specific gaps or missing provisions

6. **STRUCTURE YOUR ANSWER:**
   a) Identify applicable regulations (with citations and URLs)
   b) Quote key legal requirements (direct text from regulations)
   c) Analyze contract provisions (cite specific sections)
   d) Assess compliance (with reasoning)
   e) Identify gaps or issues

Focus on precision, not length. Every claim about the law must be cited and quoted."""

            # Generate content with Google Search grounding
            config = GenerateContentConfig(
                tools=[self.search_tool],
                temperature=0.2,
                top_p=0.8,
                top_k=40,
                max_output_tokens=8000,
                system_instruction=system_instruction
            )

            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=config
            )

            # Extract grounding metadata if available
            grounding_metadata = None
            if hasattr(response, 'grounding_metadata') and response.grounding_metadata:
                grounding_metadata = {
                    'web_search_queries': getattr(response.grounding_metadata, 'web_search_queries', []),
                    'grounding_chunks': getattr(response.grounding_metadata, 'grounding_chunks', []),
                    'search_entry_point': getattr(response.grounding_metadata, 'search_entry_point', None),
                }

            return {
                "answer": response.text,
                "model": self.model_name,
                "elapsed_seconds": time.time() - start_time,
                "grounding_metadata": grounding_metadata,
                "tokens_used": {
                    "prompt": getattr(response.usage_metadata, 'prompt_token_count', None) if hasattr(response, 'usage_metadata') else None,
                    "completion": getattr(response.usage_metadata, 'candidates_token_count', None) if hasattr(response, 'usage_metadata') else None,
                    "total": getattr(response.usage_metadata, 'total_token_count', None) if hasattr(response, 'usage_metadata') else None
                }
            }
        except Exception as e:
            import traceback
            return {
                "error": str(e),
                "error_trace": traceback.format_exc(),
                "answer": None,
                "model": self.model_name
            }

    def test_question(self, contract_file: str, question_data: dict) -> dict:
        """Test one question with Gemini."""
        print(f"\n{'='*80}")
        print(f"Testing: {question_data['qa_id']} - {question_data['question_type']}")
        print(f"Contract: {contract_file}")
        print(f"{'='*80}\n")

        # Read FULL contract
        full_contract = self.read_contract(contract_file)
        print(f"Using FULL contract: {len(full_contract):,} chars\n")

        question = question_data['question_text']

        result = {
            "qa_id": question_data['qa_id'],
            "question_type": question_data['question_type'],
            "regulation_focus": question_data['regulation_focus'],
            "contract_file": contract_file,
            "contract_size_chars": len(full_contract),
            "question": question,
            "expected_answer": question_data['expected_answer'],
            "expected_citation": question_data['expected_citation'],
            "response": {}
        }

        # Test Gemini
        if self.client:
            print("Querying Gemini with Google Search grounding (Vertex AI)...")
            result['response'] = self.query_gemini(full_contract, question)
            if 'error' in result['response'] and result['response']['error']:
                print(f"✗ Gemini error: {result['response']['error']}")
                if 'error_trace' in result['response']:
                    print(f"  Trace: {result['response']['error_trace']}")
            else:
                print(f"✓ Gemini ({result['response'].get('elapsed_seconds', 0):.1f}s)")
                tokens = result['response'].get('tokens_used', {})
                if tokens and tokens.get('total'):
                    print(f"  Tokens: {tokens.get('total', 0):,}")
                grounding = result['response'].get('grounding_metadata')
                if grounding:
                    search_queries = grounding.get('web_search_queries', [])
                    chunks = grounding.get('grounding_chunks', [])
                    print(f"  Search queries: {len(search_queries)}")
                    print(f"  Grounding chunks: {len(chunks)}")

        return result


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Gemini Vertex AI Test with Google Search Grounding')
    parser.add_argument('--rate-limit', type=float, default=15.0,
                        help='Seconds to wait between questions (default: 15.0)')
    parser.add_argument('--questions', type=str, default='all',
                        help='Which questions to test: "all" or comma-separated IDs like "1A,5A"')
    parser.add_argument('--project-id', type=str,
                        help='Google Cloud Project ID (or set GOOGLE_CLOUD_PROJECT env var)')
    parser.add_argument('--location', type=str, default='us-central1',
                        help='Google Cloud location (default: us-central1)')
    args = parser.parse_args()

    print("\n" + "="*80)
    print("GEMINI VERTEX AI TEST - GOOGLE SEARCH GROUNDING")
    print("="*80)
    print("\nModel: Gemini 2.0 Flash (Experimental)")
    print("Platform: Vertex AI")
    print("Search: Google Search Grounding ENABLED")
    print(f"Rate limit: {args.rate_limit}s between questions\n")

    tester = GeminiVertexTester(
        project_id=args.project_id,
        location=args.location
    )

    if not tester.client:
        print("\n" + "="*80)
        print("ERROR: Vertex AI not initialized")
        print("="*80)
        print("\nRequired setup:")
        print("1. Set GOOGLE_CLOUD_PROJECT in .env or use --project-id flag")
        print("2. Authenticate: gcloud auth application-default login")
        print("3. Enable Vertex AI API in your Google Cloud project")
        return

    # All 6 test questions
    all_questions = [
        {
            "qa_id": "1A",
            "question_type": "Data Processing Permissions",
            "regulation_focus": "GDPR, EU AI Act, Data Protection",
            "contract_file": "FOUNDATIONMEDICINE,INC_02_02_2015-EX-10.2-Collaboration Agreement.txt",
            "question_text": "Are we permitted to process the genomic data of our customers?",
            "expected_answer": "Analysis should cover GDPR Article 6 and Article 9 (special category data), consent requirements, data processing agreements, cross-border transfer mechanisms",
            "expected_citation": "GDPR Articles 6, 9; Contract data processing clauses"
        },
        {
            "qa_id": "1B",
            "question_type": "Data Governance Compliance",
            "regulation_focus": "GDPR, EU AI Act Article 10",
            "contract_file": "FOUNDATIONMEDICINE,INC_02_02_2015-EX-10.2-Collaboration Agreement.txt",
            "question_text": "Is this contract compliant with current data governance rules? If not, what is missing?",
            "expected_answer": "Should assess GDPR data governance requirements, EU AI Act Article 10, data quality standards, bias detection/mitigation, record-keeping obligations",
            "expected_citation": "GDPR; Regulation (EU) 2024/1689, Article 10"
        },
        {
            "qa_id": "2A",
            "question_type": "Brexit Amendments",
            "regulation_focus": "UK REUL Act 2023, Post-Brexit Regulatory Divergence",
            "contract_file": "WPPPLC_04_30_2020-EX-4.28-SERVICE AGREEMENT.txt",
            "question_text": "Do any amendments need to be made on account of Brexit?",
            "expected_answer": "Should identify references to EU regulations that are now UK-retained law, GDPR vs UK GDPR differences, data transfer mechanisms between UK and EU",
            "expected_citation": "UK REUL Act 2023; UK GDPR; FCA guidance on retained EU law"
        },
        {
            "qa_id": "3A",
            "question_type": "California Data Protection Compliance",
            "regulation_focus": "California CPRA, CPPA ADMT Regulations",
            "contract_file": "CardlyticsInc_20180112_S-1_EX-10.16_11002987_EX-10.16_Maintenance Agreement1.txt",
            "question_text": "Is this contract compliant with data protection laws in California?",
            "expected_answer": "Should assess CPRA compliance, ADMT regulations (Nov 2024), risk assessment obligations, consumer opt-out rights, service provider requirements",
            "expected_citation": "California CPRA (Civil Code § 1798.100 et seq.); CPPA ADMT regulations (Nov 2024)"
        },
        {
            "qa_id": "4A",
            "question_type": "ESG Compliance Assessment",
            "regulation_focus": "EU CSDDD, ESG Standards",
            "contract_file": "UpjohnInc_20200121_10-12G_EX-2.6_11948692_EX-2.6_Manufacturing Agreement_ Supply Agreement.txt",
            "question_text": "Assess this agreement for ESG compliance.",
            "expected_answer": "Should evaluate EU CSDDD compliance (Directive 2024/1760), supply chain monitoring, labor standards enforcement, environmental impact, grievance mechanisms, Scope 3 emissions tracking",
            "expected_citation": "Directive (EU) 2024/1760 (CSDDD), Articles 7-8, 15; ISO ESG standards"
        },
        {
            "qa_id": "5A",
            "question_type": "Non-Compete Validity",
            "regulation_focus": "FTC Non-Compete Ban, State Law",
            "contract_file": "MEDALISTDIVERSIFIEDREIT,INC_05_18_2020-EX-10.1-CONSULTING AGREEMENT.txt",
            "question_text": "Is the non-compete clause valid?",
            "expected_answer": "Should analyze FTC non-compete ban status (finalized August 2024, currently enjoined), senior executive exception, contractor vs employee status, applicable state law, reasonableness of scope/duration/geography",
            "expected_citation": "FTC Rule 16 CFR § 910; Ryan LLC v. FTC (August 2024 injunction); Virginia state law on non-competes"
        }
    ]

    # Filter questions if specified
    if args.questions != 'all':
        requested_ids = [q.strip() for q in args.questions.split(',')]
        test_questions = [q for q in all_questions if q['qa_id'] in requested_ids]
        if not test_questions:
            print(f"Error: No questions found matching: {args.questions}")
            return
    else:
        test_questions = all_questions

    print(f"Testing {len(test_questions)} question(s): {', '.join(q['qa_id'] for q in test_questions)}\n")

    results = []
    for i, question in enumerate(test_questions, 1):
        print(f"\n[{i}/{len(test_questions)}] Starting test...")
        result = tester.test_question(question['contract_file'], question)
        results.append(result)

        if i < len(test_questions):
            print(f"\nWaiting {args.rate_limit} seconds before next test...")
            time.sleep(args.rate_limit)

    # Save JSON results
    output_data = {
        "test_date": datetime.now().isoformat(),
        "test_type": "gemini_vertex_search_grounding",
        "model": "gemini-2.0-flash-exp",
        "platform": "vertex_ai",
        "project_id": tester.project_id,
        "location": tester.location,
        "description": "Gemini with Vertex AI Google Search grounding for legal research",
        "total_questions": len(results),
        "results": results
    }

    json_file = "gemini_vertex_results.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*80}")
    print("✓ Gemini Vertex AI Search Grounding Test complete!")
    print(f"\nResults saved to: {json_file}")
    print(f"Tested {len(results)} questions")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
