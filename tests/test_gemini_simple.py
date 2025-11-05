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

            system_instruction = """You are a senior legal research AI assistant with real-time Google Search capabilities, specializing in contract analysis and regulatory compliance.

Your task is to provide COMPREHENSIVE, well-cited legal analysis. You MUST:

1. **Find ALL current, applicable law** - Use Google Search extensively to locate:
   - Federal regulations, statutes, and recent rules (as of November 5, 2025)
   - State-specific laws and recent amendments
   - Recent court decisions and injunctions
   - Agency guidance and interpretations
   - International regulations if applicable (EU, UK, etc.)

2. **Provide COMPLETE analysis with pinpoint citations** - For every legal requirement:
   - Exact citation: "GDPR Article 9(2)(a)", "16 CFR § 910.2(a)(1)", "Cal. Civ. Code § 1798.140(ag)(1)"
   - Effective date and status (active, enjoined, amended)
   - Direct quote from the legal text (not summaries)
   - Official source URL

3. **Include ALL relevant context** - Your analysis should cover:
   - Historical context (previous versions of law, amendments)
   - Current legal status (in effect, enjoined, challenged)
   - Exceptions and exemptions
   - Industry-specific applications
   - Conflicting regulations and how to resolve them
   - Pending legislation that may affect compliance

4. **Thorough contract analysis** - For each provision:
   - Quote the exact contract language (with section numbers)
   - Compare against legal requirements point-by-point
   - Identify compliance status: compliant, partially compliant, non-compliant, unclear
   - List ALL missing provisions or gaps
   - Note ambiguous language that could create risk

5. **Structure your answer comprehensively**:
   a) Executive Summary (2-3 sentences)
   b) Applicable Regulations (with full citations, dates, URLs)
   c) Key Legal Requirements (direct quotes from each regulation)
   d) Detailed Contract Analysis (quote and analyze each relevant section)
   e) Compliance Assessment (comprehensive evaluation)
   f) Identified Gaps and Missing Provisions
   g) Recommendations (what needs to be added/changed)
   h) Risk Assessment (potential consequences of non-compliance)

6. **Use Google Search extensively** - Search multiple times for:
   - Primary sources of law
   - Recent amendments and updates
   - Court cases and injunctions
   - Regulatory guidance
   - Cross-references and related regulations

Your answers should be THOROUGH, not brief. Legal analysis requires comprehensive coverage. Include ALL relevant information, not just highlights."""

            prompt = f"""You are analyzing a legal contract for regulatory compliance. Provide a COMPREHENSIVE legal analysis.

═══════════════════════════════════════════════════════════════════════════════
FULL CONTRACT TEXT (READ CAREFULLY):
═══════════════════════════════════════════════════════════════════════════════

{contract_text}

═══════════════════════════════════════════════════════════════════════════════
LEGAL QUESTION TO ANALYZE:
═══════════════════════════════════════════════════════════════════════════════

{question}

═══════════════════════════════════════════════════════════════════════════════
MANDATORY REQUIREMENTS FOR YOUR ANALYSIS:
═══════════════════════════════════════════════════════════════════════════════

1. **COMPREHENSIVE LEGAL RESEARCH (as of November 5, 2025):**

   Use Google Search EXTENSIVELY to find:

   a) ALL applicable federal regulations
      - Search: "[topic] federal regulations 2025"
      - Search: "FTC [topic] rule 2024 2025"
      - Search: "[agency] final rule [topic]"

   b) ALL applicable state laws
      - Search: "[state] [topic] law 2025"
      - Search: "[state] code section [topic]"

   c) Recent amendments and changes
      - Search: "[regulation name] amended 2024 2025"
      - Search: "[regulation] effective date"

   d) Court challenges and injunctions
      - Search: "[regulation name] court injunction 2024"
      - Search: "[regulation name] enjoined stayed"

   e) International regulations (if applicable)
      - Search: "EU [topic] regulation 2024"
      - Search: "GDPR AI Act 2024"

2. **DETAILED CITATIONS WITH COMPLETE CONTEXT:**

   For EVERY regulation mentioned, provide:
   - Full citation: "Title, CFR Part, Section, Subsection"
   - Effective date: "Effective [date]" or "Finalized [date], currently enjoined"
   - Current status: "In force", "Enjoined", "Under review"
   - Direct quote: The actual text from the regulation (3-5 sentences minimum)
   - Official URL: Link to ecfr.gov, eur-lex.europa.eu, state .gov sites

   Example format:
   ```
   **FTC Non-Compete Clause Rule (16 CFR Part 910)**
   - Finalized: August 20, 2024
   - Status: Currently enjoined nationwide by U.S. District Court (Ryan LLC v. FTC, August 2024)
   - Scheduled effective date: September 4, 2024 (not in effect)
   - URL: https://www.ecfr.gov/current/title-16/part-910

   The rule states:
   "It is an unfair method of competition for an employer to enter into or attempt to
   enter into a non-compete clause with a worker; to enforce or attempt to enforce a
   non-compete clause with a worker; or to represent to a worker that the worker is
   subject to a non-compete clause where the employer has no good faith basis to
   believe that the worker is subject to an enforceable non-compete clause."

   Exception under 16 CFR § 910.3(a):
   "This rule does not apply to a non-compete clause that is entered into by a person
   pursuant to a bona fide sale of a business entity, of the person's ownership interest
   in a business entity, or of all or substantially all of a business entity's operating assets."

   Senior executive exception under 16 CFR § 910.3(b):
   [Include if applicable]
   ```

3. **THOROUGH CONTRACT ANALYSIS:**

   For EACH relevant contract provision:

   a) Quote the exact contract language:
      "Section [X.X] states: '[exact text from contract]'"

   b) Identify which legal requirement it addresses:
      "This provision relates to [specific regulation, citation]"

   c) Analyze compliance in detail:
      - Does it fully comply? Why or why not?
      - What specific elements are present/missing?
      - How does the language compare to the legal requirement?

   d) Assess gaps:
      - What additional provisions are required by law but missing?
      - What provisions are present but inadequate?
      - What provisions conflict with legal requirements?

4. **STRUCTURE YOUR COMPLETE ANSWER:**

   **A. EXECUTIVE SUMMARY** (3-5 sentences)
   Brief overview of findings and overall compliance status.

   **B. APPLICABLE REGULATIONS** (Comprehensive list with full details)
   List ALL relevant regulations with:
   - Full citation
   - Effective date and current status
   - Primary source URL
   - Brief description of what it covers

   **C. KEY LEGAL REQUIREMENTS** (Quote extensively from each regulation)
   For each major regulation:
   - Quote the key provisions (full text, not summaries)
   - Explain what compliance requires
   - Note any exceptions or safe harbors

   **D. DETAILED CONTRACT ANALYSIS** (Section by section)
   For each relevant contract section:
   - Quote the contract provision
   - Identify which legal requirement it addresses
   - Analyze compliance status
   - Note strengths and weaknesses

   **E. COMPLIANCE ASSESSMENT** (Overall evaluation)
   - What is compliant?
   - What is partially compliant? (explain the gap)
   - What is non-compliant? (explain the violation)
   - What is unclear or ambiguous?

   **F. IDENTIFIED GAPS AND MISSING PROVISIONS** (Complete list)
   List ALL missing requirements:
   - What provisions are required by law but absent?
   - What disclosures are required but missing?
   - What procedures are required but not documented?

   **G. RECOMMENDATIONS** (Specific, actionable)
   - What specific language should be added?
   - What provisions should be modified?
   - What additional agreements or notices are needed?

   **H. RISK ASSESSMENT** (Consequences of non-compliance)
   - Legal risks
   - Regulatory enforcement risks
   - Financial penalties
   - Business impact

5. **QUALITY REQUIREMENTS:**

   - Minimum 2,000 words for comprehensive analysis
   - Use Google Search at least 5-10 times
   - Cite at least 5-10 specific legal sources
   - Quote actual legal text (not summaries) for each key requirement
   - Provide official URLs for ALL major regulations cited
   - Reference specific contract sections by number
   - Be thorough, not brief - legal analysis requires detail

6. **VERIFICATION:**

   Before submitting your answer, verify:
   - [ ] Have I searched for ALL applicable laws and regulations?
   - [ ] Have I included the current status (effective, enjoined, etc.)?
   - [ ] Have I quoted the actual legal text (not paraphrased)?
   - [ ] Have I provided official URLs for sources?
   - [ ] Have I analyzed EACH relevant contract provision?
   - [ ] Have I identified ALL gaps and missing provisions?
   - [ ] Is my analysis comprehensive (2,000+ words)?

═══════════════════════════════════════════════════════════════════════════════
BEGIN YOUR COMPREHENSIVE ANALYSIS:
═══════════════════════════════════════════════════════════════════════════════"""

            # Generate content with Google Search grounding
            config = GenerateContentConfig(
                tools=[self.search_tool],
                temperature=0.2,
                top_p=0.8,
                top_k=40,
                max_output_tokens=6000,  # Matches Perplexity for fair comparison
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
    print("GEMINI-SIMPLE TEST - MATCHES PERPLEXITY SETUP")
    print("="*80)
    print("\nModel: Gemini 2.0 Flash (Experimental)")
    print("Platform: Vertex AI")
    print("Search: Google Search Grounding ENABLED")
    print("Config: Same prompt/tokens as Perplexity (6000 tokens)")
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
        "test_type": "gemini_simple_perplexity_match",
        "model": "gemini-2.0-flash-exp",
        "platform": "vertex_ai",
        "project_id": tester.project_id,
        "location": tester.location,
        "config": "Same prompt and 6000 token limit as Perplexity for fair comparison",
        "description": "Gemini with Vertex AI Google Search grounding - MATCHES PERPLEXITY SETUP",
        "total_questions": len(results),
        "results": results
    }

    json_file = "gemini_simple_results.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*80}")
    print("✓ Gemini-Simple Test complete!")
    print(f"\nResults saved to: {json_file}")
    print(f"Tested {len(results)} questions")
    print("\nThis test MATCHES Perplexity setup for fair comparison:")
    print("- Same prompt structure")
    print("- Same token limit (6000)")
    print("- Same temperature (0.2)")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
