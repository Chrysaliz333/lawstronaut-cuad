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
├── LAWSTRONAUT_TEST_MATRIX.md        # Detailed test questions (893 lines)
├── SUPABASE_SETUP.md                 # Proposed backend architecture
├── CUAD_v1_README.txt                # Dataset documentation
│
├── data/                             # Large data files (not in git)
│   ├── CUAD_v1.json                  # 40MB - SQuAD format dataset
│   ├── master_clauses.csv            # 3.8MB - Contract metadata
│   ├── full_contract_pdf/            # 510 PDF contracts
│   ├── full_contract_txt/            # 510 text contracts
│   └── label_group_xlsx/             # CUAD clause labels
│
├── tests/                            # Test harness code
│   ├── test_gemini_vertex.py        # Vertex AI + search grounding
│   ├── VERTEX_AI_APPLICATION_PROMPT.md
│   └── PROJECT_SUMMARY.md           # Gemini evaluation results
│
├── deploy/                           # GCP deployment (incomplete)
│   ├── Dockerfile
│   ├── cloudbuild.yaml
│   └── setup-gcp.sh
│
└── docs/                             # Additional documentation
    └── Lawstronaut questions.xlsx    # Test questions spreadsheet
```

## Setup (Incomplete)

### Prerequisites
```bash
# Python 3.10+
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies (TODO: create requirements.txt)
pip install google-genai pandas python-dotenv
```

### Environment Variables
Create `.env` file:
```bash
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
OPENAI_API_KEY=sk-...
```

### Data Setup
Large data files are **not in git**. Download separately:
- CUAD dataset: https://github.com/TheAtticusProject/cuad
- Place in `data/` directory

## Testing Gemini (Current Focus)

```bash
cd tests/
python test_gemini_vertex.py --questions=5A --rate-limit=15
```

**Key Finding**: Free Gemini API lacks Google Search grounding, missing 2024 regulations. Vertex AI required for production legal analysis.

## Known Issues

1. **No proper Python package** - scattered scripts, no imports
2. **Missing dependencies** - no requirements.txt
3. **Incomplete test suite** - test_llm_apis.py doesn't exist
4. **Data files in git** - should use Git LFS or external storage
5. **Mixed concerns** - GCP deployment mixed with research code
6. **No application code** - only test harnesses

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
