# Exact Test Questions for Perplexity Comparison

## Question Format

**IMPORTANT:** These are the exact questions used in the Gemini tests. For fair comparison with Perplexity, use these EXACT questions word-for-word.

---

## Q1A: Data Processing Permissions
**Contract:** Foundation Medicine Collaboration Agreement (169KB)
**Question:**
```
Are we permitted to process the genomic data of our customers?
```
**Expected Coverage:** GDPR Article 6 & 9, EU AI Act, consent requirements, data processing agreements

---

## Q1B: Data Governance Compliance
**Contract:** Foundation Medicine Collaboration Agreement (same file as Q1A)
**Question:**
```
Is this contract compliant with current data governance rules? If not, what is missing?
```
**Expected Coverage:** GDPR, EU AI Act Article 10 (Reg 2024/1689), data quality, bias detection

---

## Q2A: Brexit Amendments
**Contract:** WPP PLC Service Agreement (65KB)
**Question:**
```
Do any amendments need to be made on account of Brexit?
```
**Expected Coverage:** UK REUL Act 2023, UK GDPR vs EU GDPR, data transfer mechanisms

---

## Q3A: California Data Protection
**Contract:** Cardlytics Maintenance Agreement (162KB)
**Question:**
```
Is this contract compliant with data protection laws in California?
```
**Expected Coverage:** CPRA, CPPA ADMT regulations (Nov 2024), risk assessments, consumer rights

---

## Q4A: ESG Compliance
**Contract:** Upjohn Manufacturing Agreement (221KB)
**Question:**
```
Assess this agreement for ESG compliance.
```
**Expected Coverage:** EU CSDDD (Directive 2024/1760), supply chain monitoring, labor standards

---

## Q5A: Non-Compete Validity ⭐ CRITICAL TEST
**Contract:** Medalist Diversified Consulting Agreement (24KB)
**Question:**
```
Is the non-compete clause valid?
```
**Expected Coverage:** FTC non-compete ban (16 CFR § 910, Aug 2024), Ryan LLC v. FTC injunction, Virginia state law

**Why This is Critical:** The FTC finalized this rule on August 20, 2024 - AFTER most LLM training cutoffs. If the model can't find this, search grounding isn't working.

---

## For Perplexity Testing

### Option 1: Test Question Only (Without Contract)
Just ask Perplexity the question directly:
```
Is the non-compete clause valid?
```

See if it provides useful legal analysis without the contract text.

### Option 2: Test with Contract Context (Recommended)
Paste the contract text, then ask:
```
[paste contract text here]

Is the non-compete clause valid?
```

### Option 3: Test with Additional Context
```
[paste contract text here]

This is a consulting agreement from May 2020 with a non-compete clause.
The consultant is based in Virginia.

Is the non-compete clause valid?
```

---

## Comparison Checklist

For each question, compare:

| Criterion | Perplexity | Gemini Vertex | Winner |
|-----------|-----------|---------------|---------|
| **Found FTC ban (Aug 2024)?** | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| **Cited 16 CFR § 910?** | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| **Mentioned Ryan LLC injunction?** | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| **Direct quotes from law?** | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| **Official source URLs?** | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| **Contract section references?** | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| **Comprehensive (1000+ words)?** | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| **Response time** | ___ sec | ___ sec | |
| **Cost per query** | $___ | $___ | |

---

## Did You Use Different Questions in Perplexity?

If you used different questions or phrasing in your Perplexity tests, please:

1. Share what questions you actually used
2. We can either:
   - Re-run Gemini with your exact questions, OR
   - Re-run Perplexity with these exact questions

**For fair comparison, the questions should be identical.**

---

## Contract Files Location

All test contracts are in: `data/test_contracts/`

You can download them from:
- GitHub: https://github.com/Chrysaliz333/lawstronaut-cuad/tree/claude/review-and-comment-011CUqKaVknRtjcuyTjmXSvJ/data/test_contracts
- Cloud Shell: `~/lawstronaut-cuad/data/test_contracts/`

To copy a contract for Perplexity testing:
```bash
cat data/test_contracts/MEDALISTDIVERSIFIEDREIT,INC_05_18_2020-EX-10.1-CONSULTING\ AGREEMENT.txt
```

---

## Questions About Your Perplexity Tests

1. **What exact questions did you ask Perplexity?**
2. **Did you paste the contract text, or just ask the question?**
3. **Which Perplexity model did you use?** (Free, Pro, API?)
4. **Did Perplexity find the FTC non-compete ban from August 2024?**
5. **Do you want to re-run either test to ensure identical questions?**
