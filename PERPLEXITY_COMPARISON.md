# Gemini vs Perplexity Comparison

## Setup

This project is now configured to compare Gemini (with Vertex AI Google Search grounding) against Perplexity for legal contract analysis.

### Test Contracts (5 files, 644KB)

All test contracts are in `data/test_contracts/`:

1. **Foundation Medicine** (169KB) - Q1A, Q1B
2. **WPP PLC** (65KB) - Q2A
3. **Cardlytics** (162KB) - Q3A
4. **Upjohn** (221KB) - Q4A
5. **Medalist Diversified** (24KB) - Q5A

### Test Questions (6 questions)

| ID | Question Type | Regulation Focus | Contract | Key Test |
|----|--------------|------------------|----------|----------|
| **Q1A** | Data Processing Permissions | GDPR, EU AI Act | Foundation Medicine | Can it cite GDPR Art 9? |
| **Q1B** | Data Governance Compliance | EU AI Act Article 10 | Foundation Medicine | Does it find EU AI Act Reg 2024/1689? |
| **Q2A** | Brexit Amendments | UK REUL Act 2023 | WPP PLC | Does it understand UK vs EU law? |
| **Q3A** | California Data Protection | CPRA, ADMT regs (Nov 2024) | Cardlytics | Does it find Nov 2024 CPPA regs? |
| **Q4A** | ESG Compliance | EU CSDDD (2024) | Upjohn | Does it cite Directive 2024/1760? |
| **Q5A** | Non-Compete Validity | FTC ban (Aug 2024) | Medalist | **Critical:** Does it find 16 CFR § 910? |

### Critical Success Criteria

The **minimum requirement** for success is finding regulations enacted **after LLM training cutoffs**:

- ✅ FTC Non-Compete Ban (16 CFR § 910) - finalized Aug 20, 2024
- ✅ EU AI Act (Regulation 2024/1689) Article 10 - Aug 1, 2024
- ✅ CPPA ADMT Regulations - Nov 2024
- ✅ EU CSDDD (Directive 2024/1760) - May 2024

If the system **cannot find the FTC non-compete ban in Q5A**, search grounding is not working.

## Running the Comparison

### 1. Run Gemini Tests

```bash
# Setup (if not already done)
pip install -r requirements.txt

# Create .env file
cat > .env << 'EOF'
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
EOF

# Authenticate with Google Cloud
gcloud auth application-default login

# Run all 6 tests
python tests/test_gemini_vertex.py --questions=all --rate-limit=15

# Or run one question at a time
python tests/test_gemini_vertex.py --questions=5A --rate-limit=15
```

**Output:** `gemini_vertex_results.json`

### 2. Compare with Perplexity

You mentioned you've already run these tests in Perplexity. Compare the outputs:

#### Key Comparison Metrics

| Metric | What to Check |
|--------|---------------|
| **Regulatory Currency** | Does it cite 2024 regulations? |
| **Citation Precision** | Pinpoint citations (e.g., "Article 9(2)(a)") or vague? |
| **Direct Quotes** | Actual legal text in quotes, or paraphrases? |
| **Primary Sources** | Official URLs (eur-lex.europa.eu, ecfr.gov)? |
| **Contract Analysis** | Specific section numbers referenced? |
| **Compliance Assessment** | Clear compliant/non-compliant determination? |
| **Gaps Identified** | Missing provisions called out? |

#### Expected Performance

**Gemini (Free API - No Grounding):**
- ❌ Misses FTC non-compete ban (training cutoff before Aug 2024)
- ❌ Misses EU AI Act specifics
- ❌ May hallucinate regulations
- ⚠️ Generic legal advice without current law

**Gemini (Vertex AI with Google Search Grounding):**
- ✅ Should find FTC non-compete ban
- ✅ Should cite EU AI Act Article 10
- ✅ Should reference CPPA ADMT regulations
- ✅ Real-time legal research capabilities

**Perplexity (Your Results):**
- Depends on which model and search settings used
- Perplexity has built-in web search

### 3. Side-by-Side Analysis Template

For each question, compare:

```markdown
## Q5A: Non-Compete Validity

**Contract:** Medalist Diversified Consulting Agreement (24KB)
**Question:** "Is the non-compete clause valid?"

### Perplexity Results
- Found FTC ban? [Yes/No]
- Citation accuracy: [Exact/Close/Vague]
- Direct quotes: [Yes/No]
- Primary source URLs: [Count]
- Contract section refs: [Yes/No]
- Processing time: [X seconds]

### Gemini Vertex Results
- Found FTC ban? [Yes/No]
- Citation accuracy: [Exact/Close/Vague]
- Direct quotes: [Yes/No]
- Primary source URLs: [Count]
- Contract section refs: [Yes/No]
- Processing time: [X seconds]
- Tokens used: [X]

### Winner: [Perplexity / Gemini / Tie]

**Reasoning:** [Why one performed better]
```

## Cost Comparison

### Gemini Vertex AI
- Input: $0.075 per 1M tokens
- Output: $0.30 per 1M tokens
- **Google Search grounding: $35 per 1,000 queries** 🔥
- Estimated 6 questions: ~$0.22

### Perplexity
- Free tier: 5 searches/4 hours
- Pro: $20/month unlimited
- API: Variable pricing

## Key Findings to Document

### Regulatory Detection (Post-Cutoff)
- [ ] FTC Non-Compete Ban (Aug 2024) - Q5A
- [ ] EU AI Act Article 10 (Reg 2024/1689) - Q1B
- [ ] CPPA ADMT Regulations (Nov 2024) - Q3A
- [ ] EU CSDDD (Directive 2024/1760) - Q4A
- [ ] UK REUL Act 2023 - Q2A

### Citation Quality
- [ ] Precise statutory citations (e.g., "Cal. Civ. Code § 1798.140(ag)(1)")
- [ ] Direct quotes from legal text (not summaries)
- [ ] Official government URLs

### Contract Analysis
- [ ] References specific contract sections by number
- [ ] Identifies compliant vs non-compliant provisions
- [ ] Lists missing requirements

### Comparison Verdict

**Overall Winner:** [To be determined]

**Best for:**
- Perplexity: [Use cases where it excels]
- Gemini Vertex: [Use cases where it excels]

**Cost-Benefit:**
- Perplexity: [Cost vs accuracy tradeoff]
- Gemini Vertex: [Cost vs accuracy tradeoff]

## Next Steps

1. Run Gemini tests with `python tests/test_gemini_vertex.py --questions=all`
2. Review `gemini_vertex_results.json`
3. Compare with your Perplexity results
4. Document findings in this file or create a new comparison report
5. Decide which tool is better for your legal research use case

## Questions to Answer

- Which model has more current regulatory knowledge?
- Which provides better citation accuracy?
- Which is more cost-effective for legal research?
- Which would you use for production legal intelligence?
