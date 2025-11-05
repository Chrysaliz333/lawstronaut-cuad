# Lawstronaut CUAD

**Legal contract intelligence using LLMs with post-cutoff regulatory retrieval.**

## Status: Research/Testing Phase

This project evaluates LLM capabilities for analyzing legal contracts against regulations enacted after LLM training cutoff dates (GPT-4: Apr 2023, Claude: Apr 2024).

## Overview

- **Dataset**: CUAD v1 (510 commercial contracts from SEC EDGAR filings)
- **Focus**: Testing LLM awareness of 2023-2024 regulatory changes:
  - EU AI Act (Aug 2024)
  - FTC Non-Compete Ban (Aug 2024, currently enjoined)
  - UK Retained EU Law (REUL) Act changes
  - US State AI laws (Colorado SB 24-205, California AB 2013)
  - EU Corporate Sustainability Due Diligence Directive (CSDDD)

## Current State

⚠️ **This is research/exploration code, not a production application.**

What exists:
- CUAD dataset (contracts + analysis metadata)
- Test questions matrix for evaluating LLM regulatory knowledge
- Gemini Vertex AI test harness (incomplete)
- Documentation of potential architecture (Supabase backend)

What doesn't exist:
- Working application
- Proper Python package structure
- Completed test suite
- Production backend

## Project Structure

```
lawstronaut-cuad/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore patterns
├── CLEANUP_PLAN.md                    # Cleanup documentation
│
├── src/                               # Application source code
│   └── lawstronaut/
│       └── __init__.py
│
├── tests/                             # Test harness code
│   ├── __init__.py
│   ├── test_llm_apis.py              # Base LLM tester class
│   └── test_gemini_vertex.py         # Vertex AI + Google Search grounding
│
├── docs/                              # Documentation
│   ├── PROJECT_SUMMARY.md            # Gemini evaluation results
│   ├── VERTEX_AI_APPLICATION_PROMPT.md  # Vertex AI setup guide
│   ├── LAWSTRONAUT_TEST_MATRIX.md    # Detailed test questions (893 lines)
│   ├── SUPABASE_SETUP.md             # Proposed backend architecture
│   └── questions.xlsx                # Test questions spreadsheet
│
├── data/                              # Large data files (NOT in git)
│   ├── README.md                     # Data download instructions
│   ├── CUAD_v1_README.txt            # Dataset documentation
│   ├── CUAD_v1.json                  # 40MB - SQuAD format dataset (ignored)
│   ├── master_clauses.csv            # 3.8MB - Contract metadata (ignored)
│   ├── full_contract_pdf/            # 510 PDF contracts (ignored)
│   ├── full_contract_txt/            # 510 text contracts (ignored)
│   └── label_group_xlsx/             # CUAD clause labels (ignored)
│
├── deploy/                            # GCP deployment (incomplete)
│   ├── README.md                     # Deployment notes
│   ├── Dockerfile
│   ├── cloudbuild.yaml
│   └── setup-gcp.sh
│
└── scripts/                           # Utility scripts (TODO)
```

## Setup

### Prerequisites
```bash
# Python 3.10+
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables
Create `.env` file in project root:
```bash
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
# Optional:
# OPENAI_API_KEY=sk-...
# ANTHROPIC_API_KEY=sk-ant-...
```

### Data Setup
Large data files are **not in git**. See `data/README.md` for download instructions.

Quick setup:
```bash
# Download CUAD dataset
git clone https://github.com/TheAtticusProject/cuad.git /tmp/cuad

# Copy data files
cp /tmp/cuad/data/CUAD_v1.json data/
cp /tmp/cuad/data/master_clauses.csv data/
cp -r /tmp/cuad/data/full_contract_txt data/
```

## Running Tests (Current Focus)

### Test Gemini with Vertex AI

```bash
# Authenticate with Google Cloud
gcloud auth application-default login

# Run all 6 test questions
python tests/test_gemini_vertex.py --questions=all

# Run specific question (e.g., Q5A - Non-compete)
python tests/test_gemini_vertex.py --questions=5A --rate-limit=15
```

### Test Questions

1. **Q1A**: Data Processing Permissions (GDPR, EU AI Act)
2. **Q1B**: Data Governance Compliance (EU AI Act Article 10)
3. **Q2A**: Brexit Amendments (UK REUL Act 2023)
4. **Q3A**: California Data Protection (CPRA, ADMT regs)
5. **Q4A**: ESG Compliance (EU CSDDD)
6. **Q5A**: Non-Compete Validity (FTC ban)

**Key Finding**: Free Gemini API lacks Google Search grounding, missing 2024 regulations. Vertex AI required for production legal analysis. See `docs/PROJECT_SUMMARY.md` for details.

## Known Issues / Limitations

1. ✅ ~~No proper Python package~~ - **FIXED**: Proper structure created
2. ✅ ~~Missing dependencies~~ - **FIXED**: requirements.txt created
3. ✅ ~~Data files in git~~ - **FIXED**: Large files now gitignored
4. ✅ ~~Messy structure~~ - **FIXED**: Reorganized with clear directories
5. **Incomplete test suite** - Only Gemini test implemented (OpenAI, Claude TBD)
6. **No application code** - Only test harnesses, no production app
7. **GCP deployment incomplete** - Deployment configs are placeholders

## Next Steps (Proposed)

1. **Decide on scope**: Research project or production tool?
2. **Clean up structure**: Proper Python package with src/ layout
3. **Complete test suite**: Finish Gemini vs Claude vs GPT-4 comparison
4. **Extract data**: Move large files to external storage or Git LFS
5. **Implement backend**: If building production tool, implement Supabase schema
6. **Create API**: REST API for legal contract analysis with regulatory retrieval

## Related Documentation

- **LAWSTRONAUT_TEST_MATRIX.md** - 428 contracts affected by post-2023 regulations, detailed test questions
- **SUPABASE_SETUP.md** - Proposed database schema for production backend
- **tests/PROJECT_SUMMARY.md** - Gemini evaluation results (free API vs Vertex AI)

## License

Dataset: CUAD v1 is under Creative Commons Attribution 4.0 International

## Contact

This is a research/exploration project. Not ready for external use.
