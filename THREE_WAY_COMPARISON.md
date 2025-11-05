# Three-Way Comparison: Perplexity vs Gemini-Simple vs Gemini-Enhanced

## Overview

You now have **3 different test configurations** to compare:

| Test | Model | Tokens | Prompt Style | Purpose |
|------|-------|--------|--------------|---------|
| **Perplexity** | Sonar-Pro | 6,000 | "Focus on precision, not length" | Your baseline |
| **Gemini-Simple** | Gemini 2.0 Flash | 6,000 | Same as Perplexity | Fair comparison |
| **Gemini-Enhanced** | Gemini 2.0 Flash | 32,000 | "Be thorough, comprehensive, 2000+ words" | Show what's possible |

---

## Your Perplexity Results (Already Complete)

**Overall Score: 65.8/100 - FAIL**

### Critical Failures:
- **Q1A (54/100)**: Missed GDPR Article 9 → €20M fine risk
- **Q4A (40/100)**: Cited wrong regulation (AI Act instead of CSDDD)
- **Q5A (55/100)**: Didn't verify FTC rule is enjoined → invalid legal advice

### Key Issue:
**58% average recall** - finds less than 60% of applicable laws

---

## Running the Gemini Tests

### Test 1: Gemini-Simple (Fair Comparison)

**In Cloud Shell:**
```bash
cd ~/lawstronaut-cuad

# Pull latest code
git pull origin claude/review-and-comment-011CUqKaVknRtjcuyTjmXSvJ

# Run Gemini-Simple (matches Perplexity)
python tests/test_gemini_simple.py --questions=all --rate-limit=15
```

**Output:** `gemini_simple_results.json`

**This tests:** Does Gemini with same constraints perform better than Perplexity?

---

### Test 2: Gemini-Enhanced (Maximum Performance)

```bash
# Run Gemini-Enhanced (comprehensive analysis)
python tests/test_gemini_vertex.py --questions=all --rate-limit=15
```

**Output:** `gemini_vertex_results.json`

**This tests:** What's possible with better prompting and more tokens?

---

## What to Compare

### 1. Law Retrieval Completeness (Most Critical)

**Q1A - Genomic Data Processing**

Expected laws (5 required):
- [ ] GDPR Article 6 (lawful basis)
- [ ] GDPR Article 9 (special category data - **genetic data**)
- [ ] GDPR Articles 4(11), 7 (consent requirements)
- [ ] GDPR Article 28 (data processing agreements)
- [ ] GDPR Articles 44-49 (cross-border transfers)

**Perplexity:** Missed Article 9 (FAILED)

**Compare:**
- How many did Gemini-Simple find?
- How many did Gemini-Enhanced find?

---

**Q4A - ESG Compliance**

Expected:
- [ ] EU CSDDD (Directive 2024/1760) Articles 7, 8, 15
- [ ] Supply chain due diligence requirements
- [ ] Labor standards enforcement
- [ ] Environmental impact monitoring

**Perplexity:** Cited **wrong regulation** (AI Act instead of CSDDD) - CATASTROPHIC FAILURE

**Compare:**
- Did Gemini-Simple cite correct regulation?
- Did Gemini-Enhanced cite correct regulation?

---

**Q5A - Non-Compete Validity** (CRITICAL TEST)

Expected:
- [ ] FTC Rule 16 CFR § 910
- [ ] **Finalized August 20, 2024**
- [ ] **Currently enjoined** by Ryan LLC v. FTC
- [ ] Not in effect as of Nov 2025
- [ ] Virginia state law (backup)

**Perplexity:** Found FTC rule but **didn't verify enjoined status** - invalid legal advice!

**Compare:**
- Did Gemini-Simple find FTC rule?
- Did it identify enjoined status?
- Did Gemini-Enhanced provide more complete analysis?

---

### 2. Citation Quality

**Perplexity Issues:**
- Vague citations (missed article/section numbers)
- No direct quotes from legal text
- Missing primary source URLs

**Compare:**
- Do Gemini tests provide pinpoint citations?
- Do they quote actual legal text?
- Do they link to official sources?

---

### 3. Legal Status Verification

**Perplexity FAILED** to identify:
- FTC rule enjoined (Q5A)
- Recent amendments (various)
- Current effective dates

**Compare:**
- Does Gemini verify legal status?
- Does it mention court challenges?
- Does it note effective dates?

---

### 4. Completeness vs Precision Trade-off

**Perplexity (6K tokens):**
- Incomplete coverage
- Brief answers
- Missing key provisions

**Compare:**
- **Gemini-Simple (6K tokens)**: Better recall with same length?
- **Gemini-Enhanced (32K tokens)**: More complete with more space?

---

## Scoring Rubric (Same as Perplexity)

### For each question, score 0-100:

| Metric | Weight | What to Check |
|--------|--------|---------------|
| **Law Applicability** | 25 pts | Found ALL applicable laws? |
| **Retrieval Completeness** | 20 pts | All articles/sections cited? |
| **Retrieval Precision** | 15 pts | No irrelevant laws cited? |
| **Accuracy** | 15 pts | Legal status correct (enjoined, effective)? |
| **Granularity** | 10 pts | Article-level citations? |
| **Citation Quality** | 10 pts | Pinpoint citations with URLs? |
| **Direct Quotes** | 5 pts | Actual legal text quoted? |

**Grading Scale:**
- **A (90-100)**: Professional standard
- **B (80-89)**: Acceptable with gaps
- **C (70-79)**: Significant deficiencies
- **D (60-69)**: Major failures
- **F (0-59)**: Unacceptable - creates malpractice risk

**Perplexity: 65.8/100 = D grade**

---

## Quick Comparison Template

### Q5A: Non-Compete Validity (Critical Test)

| Criterion | Perplexity | Gemini-Simple | Gemini-Enhanced | Winner |
|-----------|-----------|---------------|-----------------|--------|
| **Found FTC 16 CFR § 910?** | ☐ | ☐ | ☐ | |
| **Identified enjoined status?** | ✗ FAILED | ☐ | ☐ | |
| **Cited Ryan LLC v. FTC?** | ☐ | ☐ | ☐ | |
| **Virginia state law fallback?** | ☐ | ☐ | ☐ | |
| **Direct quotes from rule?** | ☐ | ☐ | ☐ | |
| **Primary source URLs?** | ☐ | ☐ | ☐ | |
| **Contract sections analyzed?** | ☐ | ☐ | ☐ | |
| **Response length** | ___ words | ___ words | ___ words | |
| **Overall Score** | 55/100 (F) | __/100 | __/100 | |

---

## Expected Outcomes

### Hypothesis 1: Gemini-Simple vs Perplexity
With **same constraints** (6K tokens, similar prompt):
- **If Gemini-Simple scores higher:** Google Search grounding > Perplexity search
- **If Perplexity scores higher:** Perplexity's search integration is better
- **If similar scores:** Models comparable with same setup

### Hypothesis 2: Gemini-Enhanced vs Both
With **more tokens** (32K) and comprehensive prompt:
- **Should score significantly higher** on completeness
- Tests impact of prompt engineering
- Shows what's possible with proper setup

### Hypothesis 3: Critical Tests
**Q5A (Non-Compete)** is the **defining test**:
- **Pass:** Identifies FTC rule AND enjoined status
- **Fail:** Misses rule OR gives advice based on enjoined law

If Gemini finds enjoined status and Perplexity didn't, **Gemini wins decisively**.

---

## Real-World Impact

### Perplexity Failures = Malpractice Exposure

**Q1A:** Missing GDPR Article 9
- **Risk:** €20 million fine + malpractice claim
- **Impact:** Genetic data processed illegally

**Q4A:** Wrong regulation cited (AI Act instead of CSDDD)
- **Risk:** Millions wasted on wrong compliance program
- **Impact:** Directors personally liable at 5% global turnover

**Q5A:** Didn't verify enjoined status
- **Risk:** £100 million competitive loss
- **Impact:** Invalid legal advice, enforced unenforceable agreement

**These aren't edge cases - this is Fortune 500 contract review.**

---

## Cost Comparison

| Test | Per Question | 6 Questions | Notes |
|------|--------------|-------------|-------|
| **Perplexity** | ~$0.01 | ~$0.06 | Pro subscription |
| **Gemini-Simple** | ~$0.04 | ~$0.24 | 6K tokens + search |
| **Gemini-Enhanced** | ~$0.15 | ~$0.90 | 32K tokens + search |

**Value Question:**
- Is 4x cost (Perplexity → Gemini-Simple) worth avoiding malpractice?
- Is 15x cost (Perplexity → Gemini-Enhanced) worth comprehensive analysis?

**Answer:** One missed Article 9 = €20M fine. Cost is irrelevant.

---

## Next Steps

### 1. Run Both Gemini Tests
```bash
cd ~/lawstronaut-cuad
python tests/test_gemini_simple.py --questions=all --rate-limit=15
python tests/test_gemini_vertex.py --questions=all --rate-limit=15
```

### 2. Compare Results
- Download all 3 JSON files
- Compare law-by-law for each question
- Score using same rubric

### 3. Document Findings
- Which model found FTC enjoined status?
- Which model cited correct CSDDD regulation?
- Which model found GDPR Article 9?

### 4. Determine Winner
**Winner = Model with:**
- ✅ Highest law retrieval completeness
- ✅ Correct legal status identification
- ✅ No catastrophic failures (wrong regulations)

---

## Key Success Criteria

A model **PASSES** if it:
1. ✅ Finds ≥90% of applicable laws
2. ✅ Verifies legal status (enjoined vs effective)
3. ✅ Cites correct regulations (no AI Act when should be CSDDD)
4. ✅ Provides pinpoint citations and quotes
5. ✅ Analyzes contract provisions

A model **FAILS** if it:
- ❌ Misses core provisions (GDPR Article 9)
- ❌ Cites wrong regulations (AI Act instead of CSDDD)
- ❌ Doesn't verify legal status (enjoined rules)
- ❌ Below 65% law retrieval

**Perplexity: FAILED (65.8/100, 58% recall)**

**Can Gemini do better? Let's find out!** 🚀
