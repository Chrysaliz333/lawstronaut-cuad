# Vertex AI Studio Application Prompt
## Legal Contract Intelligence System with Google Search Grounding

---

## Application Overview

Build a legal contract analysis application using Vertex AI Studio that leverages Gemini 2.0 Flash with Google Search grounding to analyze contracts for regulatory compliance.

---

## Core Functionality

### Input Requirements
- **Contract Text:** Full legal contract (up to 225,000+ characters)
- **Legal Question:** Specific compliance question about the contract
- **Analysis Date:** Current date for regulatory currency (November 5, 2025)

### Output Requirements
- **Structured Legal Analysis** following this format:
  1. Applicable regulations with precise citations and official URLs
  2. Direct quotes from current legal text (not summaries)
  3. Contract provision analysis with specific section references
  4. Compliance assessment (compliant/partial/non-compliant)
  5. Identified gaps and missing provisions

### Key Capabilities
- ✓ Real-time legal research using Google Search
- ✓ Access to current regulations (2024-2025 amendments)
- ✓ Primary source verification (eur-lex.europa.eu, ecfr.gov, etc.)
- ✓ Multi-jurisdictional analysis (US, EU, UK, California)
- ✓ Direct quotation of legal provisions

---

## System Prompt for Gemini

```
You are a legal research AI assistant with real-time Google Search capabilities.

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
- Clear application to the contract provisions
```

---

## User Prompt Template

```
FULL CONTRACT TEXT:
{contract_text}

QUESTION:
{legal_question}

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

Focus on precision, not length. Every claim about the law must be cited and quoted.
```

---

## Test Questions to Implement

### Question 1A: Data Processing Permissions
**Contract:** Foundation Medicine Collaboration Agreement (172,142 chars)
**Question:** "Are we permitted to process the genomic data of our customers?"
**Expected Focus:** GDPR Article 6 & 9, EU AI Act, consent requirements, data processing agreements

### Question 1B: Data Governance Compliance
**Contract:** Foundation Medicine Collaboration Agreement
**Question:** "Is this contract compliant with current data governance rules? If not, what is missing?"
**Expected Focus:** GDPR, EU AI Act Article 10, data quality standards, bias detection

### Question 2A: Brexit Amendments
**Contract:** WPP PLC Service Agreement (65,547 chars)
**Question:** "Do any amendments need to be made on account of Brexit?"
**Expected Focus:** UK REUL Act 2023, UK GDPR vs EU GDPR, retained EU law

### Question 3A: California Data Protection
**Contract:** Cardlytics Maintenance Agreement (165,322 chars)
**Question:** "Is this contract compliant with data protection laws in California?"
**Expected Focus:** CPRA, CPPA ADMT regulations (Nov 2024), risk assessments, consumer rights

### Question 4A: ESG Compliance
**Contract:** Upjohn Manufacturing Agreement (225,094 chars)
**Question:** "Assess this agreement for ESG compliance."
**Expected Focus:** EU CSDDD (Directive 2024/1760), supply chain monitoring, labor standards, environmental impact

### Question 5A: Non-Compete Validity
**Contract:** Medalist Diversified Consulting Agreement (24,315 chars)
**Question:** "Is the non-compete clause valid?"
**Expected Focus:** FTC non-compete ban (finalized Aug 2024, currently enjoined), senior executive exception, state law

---

## Model Configuration

### Recommended Settings
- **Model:** gemini-2.0-flash-exp
- **Temperature:** 0.2 (for precise legal citations)
- **Top P:** 0.8
- **Top K:** 40
- **Max Output Tokens:** 8000
- **Tools:** Google Search grounding (ENABLED)

### Critical Feature
**Google Search Grounding MUST be enabled** to:
- Access current regulations as of November 5, 2025
- Verify recent amendments (2024-2025)
- Quote actual legal text from primary sources
- Provide official government URLs

---

## Expected Performance Metrics

### What Success Looks Like

✓ **Real-time regulatory lookups:**
- Finds FTC non-compete ban (finalized August 2024)
- Identifies EU AI Act (Regulation 2024/1689) Article 10
- Locates CPPA ADMT regulations (November 2024)
- Verifies UK REUL Act 2023 implications

✓ **Precise citations:**
- "GDPR, Regulation (EU) 2016/679, Article 9(2)(a)"
- "Cal. Civ. Code § 1798.140(ag)(1)"
- "16 CFR § 910.2(a)(1)"

✓ **Direct quotes from legal text:**
- Not summaries or paraphrases
- Exact language from regulations
- Properly attributed with quotation marks

✓ **Official source URLs:**
- https://eur-lex.europa.eu/...
- https://www.ecfr.gov/...
- https://leginfo.legislature.ca.gov/...
- https://www.legislation.gov.uk/...

✓ **Contract section analysis:**
- References specific clauses (e.g., "Section 13.8.2")
- Identifies compliance status per provision
- Lists missing requirements

### What Failure Looks Like (avoid these)

✗ Cannot access current law (uses training data only)
✗ Creates hypothetical regulations that don't exist
✗ Provides unverified URLs
✗ Quotes from memory instead of primary sources
✗ Misses major 2024 regulatory developments

---

## Implementation Steps in Vertex AI Studio

### Step 1: Create Prompt
1. Go to Vertex AI Studio → Multimodal prompts
2. Set Model: `gemini-2.0-flash-exp`
3. Enable **Grounding with Google Search**
4. Add System Instructions (see System Prompt above)

### Step 2: Configure Parameters
- Temperature: 0.2
- Output token limit: 8000
- Safety settings: Adjust as needed for legal content

### Step 3: Test with Sample
Use Question 5A (Non-Compete) as initial test:
- Shortest contract (24,315 chars)
- Most critical test: Should identify FTC non-compete ban from Aug 2024
- If it finds the FTC rule, search grounding is working

### Step 4: Create Application
Build interface that:
- Accepts contract text upload
- Presents 6 predefined questions OR custom question input
- Calls Gemini with search grounding
- Returns structured analysis
- Displays grounding metadata (search queries used, sources)

### Step 5: Validate Output
Check that responses include:
- [ ] Current law as of Nov 5, 2025
- [ ] Precise statutory citations
- [ ] Direct quotes in quotation marks
- [ ] Official government URLs
- [ ] Specific contract section references
- [ ] Compliance assessment
- [ ] Identified gaps

---

## Sample Expected Output

For Question 5A (Non-Compete Validity), the system should produce something like:

```
**a) Applicable Regulations (with Citations and URLs)**

1. **FTC Non-Compete Clause Rule:** 16 CFR Part 910
   - Finalized: August 20, 2024
   - Status: Enjoined by U.S. District Court (Ryan LLC v. FTC, August 2024)
   - URL: https://www.ecfr.gov/current/title-16/part-910

2. **Virginia Code Section 40.1-28.7:1:** Restrictions on non-compete agreements for low-wage employees
   - URL: https://law.lis.virginia.gov/vacode/title40.1/section40.1-28.7:1/

**b) Key Legal Requirements (Direct Quotes)**

FTC Rule 16 CFR § 910.2(a)(1):
"It is an unfair method of competition for an employer to enter into or attempt to enter into a non-compete clause with a worker..."

Exception under 16 CFR § 910.3(a):
"This rule does not apply to a non-compete clause that is entered into by a person pursuant to a bona fide sale of a business entity."

**c) Contract Analysis (Specific Sections)**

Section 7.3 of the Consulting Agreement contains a 12-month non-compete provision...

[Additional detailed analysis follows...]
```

---

## Success Criteria

### Critical Test: Question 5A (Non-Compete)

The application **MUST**:
1. ✓ Identify FTC non-compete ban (16 CFR Part 910)
2. ✓ Note it was finalized August 20, 2024
3. ✓ Mention Ryan LLC v. FTC injunction
4. ✓ Cite senior executive exception
5. ✓ Analyze Virginia state law applicability

If the system fails to mention the FTC rule, **Google Search grounding is not working**.

### Other Critical Tests

- **Q1B:** Must find EU AI Act (Regulation 2024/1689) Article 10
- **Q3A:** Must reference CPPA ADMT regulations from November 2024
- **Q2A:** Must discuss UK REUL Act 2023 implications
- **Q4A:** Must cite EU CSDDD (Directive 2024/1760)

---

## Cost Estimates

Based on token usage from preliminary tests:
- Average: ~30,000 tokens per question
- 6 questions: ~180,000 tokens total

**Vertex AI Pricing:**
- Gemini 2.0 Flash input: $0.075 per 1M tokens
- Gemini 2.0 Flash output: $0.30 per 1M tokens
- **Google Search grounding: $35 per 1,000 queries**

**Estimated cost for 6 questions:**
- Tokens: ~$0.01
- Search grounding: ~$0.21 (6 queries)
- **Total: ~$0.22**

---

## Contract Text Files

You will need to upload these contract files to the application:

1. `FOUNDATIONMEDICINE,INC_02_02_2015-EX-10.2-Collaboration Agreement.txt` (172,142 chars)
2. `WPPPLC_04_30_2020-EX-4.28-SERVICE AGREEMENT.txt` (65,547 chars)
3. `CardlyticsInc_20180112_S-1_EX-10.16_11002987_EX-10.16_Maintenance Agreement1.txt` (165,322 chars)
4. `UpjohnInc_20200121_10-12G_EX-2.6_11948692_EX-2.6_Manufacturing Agreement_ Supply Agreement.txt` (225,094 chars)
5. `MEDALISTDIVERSIFIEDREIT,INC_05_18_2020-EX-10.1-CONSULTING AGREEMENT.txt` (24,315 chars)

---

## Deliverables

1. **Vertex AI Studio Prompt** configured with:
   - System instructions
   - Google Search grounding enabled
   - Proper parameters (temp=0.2, max tokens=8000)

2. **Test Results** for all 6 questions showing:
   - Current law identification
   - Precise citations
   - Direct quotes
   - Primary source URLs
   - Contract analysis
   - Compliance assessment

3. **Validation Report** confirming:
   - FTC non-compete ban detected (Q5A)
   - EU AI Act Article 10 cited (Q1B)
   - CPPA ADMT regulations referenced (Q3A)
   - All grounding metadata captured

---

## Next Steps

1. **Open Vertex AI Studio:** https://console.cloud.google.com/vertex-ai/studio/multimodal?project=alien-device-432011-q6

2. **Create New Prompt:**
   - Click "Create Prompt"
   - Select Gemini 2.0 Flash
   - Enable "Grounding with Google Search"

3. **Paste System Instructions** from this document

4. **Test with Question 5A first** (shortest contract, most critical test)

5. **Verify search grounding is working** by checking if it mentions FTC non-compete ban

6. **Run all 6 questions** and compare to expected outputs

7. **Export results** and generate evaluation report

---

## Questions?

If the application doesn't find current regulations (like the FTC non-compete ban), the issue is likely:
- Google Search grounding not properly enabled
- Project permissions/API access issues
- Model selected doesn't support grounding

Contact Google Cloud Support or refer to:
https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/grounding-with-google-search
