# How to Run Tests

## Quick Start

### 1. Setup (One-Time)
```bash
# Install dependencies
pip install -r requirements.txt

# Edit .env file with your Google Cloud project ID
nano .env   # or use any editor

# Authenticate with Google Cloud (opens browser)
gcloud auth application-default login
```

### 2. Run Tests

#### Single Question (Fast - 30 seconds)
```bash
# Test Q5A - Non-Compete (CRITICAL TEST)
python tests/test_gemini_vertex.py --questions=5A --rate-limit=15
```

#### All 6 Questions (Full Suite - 3 minutes)
```bash
# Run all tests
python tests/test_gemini_vertex.py --questions=all --rate-limit=15
```

#### Specific Questions
```bash
# Run multiple specific questions
python tests/test_gemini_vertex.py --questions=1A,5A --rate-limit=15
```

---

## Available Test Questions

| ID | Question | Contract | Key Regulation |
|----|----------|----------|----------------|
| **1A** | Data Processing Permissions | Foundation Medicine | GDPR Art 6, 9 |
| **1B** | Data Governance Compliance | Foundation Medicine | EU AI Act (2024/1689) |
| **2A** | Brexit Amendments | WPP PLC | UK REUL Act 2023 |
| **3A** | California Data Protection | Cardlytics | CPRA, ADMT (Nov 2024) |
| **4A** | ESG Compliance | Upjohn | EU CSDDD (2024/1760) |
| **5A** | Non-Compete Validity | Medalist | **FTC Ban (Aug 2024)** ⭐ |

**⭐ Q5A is the critical test** - if Gemini finds the FTC non-compete ban (finalized Aug 20, 2024), then Google Search grounding is working!

---

## Command Options

```bash
python tests/test_gemini_vertex.py \
  --questions=5A \           # Which questions: "all", "1A", or "1A,2A,5A"
  --rate-limit=15 \          # Seconds between questions (avoid rate limits)
  --project-id=my-project \  # Override .env project ID
  --location=us-central1     # Override .env location
```

---

## Output

Tests create a JSON file: **`gemini_vertex_results.json`**

Contains:
- Full responses from Gemini
- Token usage statistics
- Grounding metadata (search queries used)
- Timing information

---

## What to Look For

### Success Indicators ✅
- Cites regulations from **2024** (post-cutoff)
- Precise citations: `"16 CFR § 910.2(a)(1)"`
- Direct quotes from legal text in quotation marks
- Official URLs: `https://www.ecfr.gov/...`
- References specific contract sections by number

### Failure Indicators ❌
- No mention of 2024 regulations
- Vague citations: "federal law" without specifics
- Paraphrases instead of direct quotes
- No source URLs
- Generic legal advice

---

## Troubleshooting

### Error: "GOOGLE_CLOUD_PROJECT not set"
→ Edit `.env` file and add your project ID

### Error: "Could not automatically determine credentials"
→ Run: `gcloud auth application-default login`

### Error: "Permission denied" or "API not enabled"
→ Enable Vertex AI API: https://console.cloud.google.com/apis/library/aiplatform.googleapis.com

### Error: "Rate limit exceeded"
→ Increase `--rate-limit` (e.g., `--rate-limit=30`)

### ImportError: No module named 'google'
→ Run: `pip install -r requirements.txt`

---

## Cost Estimate

**Gemini 2.0 Flash on Vertex AI:**
- Input: $0.075 per 1M tokens
- Output: $0.30 per 1M tokens
- **Google Search grounding: $35 per 1,000 queries**

**For 6 questions:**
- ~30,000 tokens total: ~$0.01
- ~6 search queries: ~$0.21
- **Total: ~$0.22**

---

## Next Steps After Running

1. **Check results:** Review `gemini_vertex_results.json`
2. **Compare with Perplexity:** See `PERPLEXITY_COMPARISON.md`
3. **Analyze findings:** Which model found 2024 regulations?
4. **Document winner:** Update comparison guide with your results
