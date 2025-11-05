# Lawstronaut CUAD - Cleanup Plan

## Current Problems

### 1. Repository Structure Issues
- ❌ Huge data files (270MB+) tracked in git
- ❌ .DS_Store and Excel lock files committed
- ❌ Folder with spaces ("TEST DATA") - bad practice
- ❌ No clear separation of code vs data vs docs
- ❌ No root README.md

### 2. Python Project Issues
- ❌ No requirements.txt or pyproject.toml
- ❌ No proper package structure
- ❌ Import errors (test_gemini_vertex.py imports non-existent modules)
- ❌ No virtual environment setup documented

### 3. Scope Confusion
- ❌ 4 different projects mixed together:
  1. CUAD dataset analysis
  2. Gemini/Vertex AI testing
  3. GCP cloud deployment
  4. Supabase backend architecture (only docs, no code)

### 4. Documentation Chaos
- ❌ No root README
- ❌ PROJECT_SUMMARY.md buried in "TEST DATA"
- ❌ 893-line test matrix (too verbose)
- ❌ 892-line Supabase setup guide (for non-existent backend)

---

## Proposed New Structure

```
lawstronaut-cuad/
│
├── README.md                         # ✅ Created - Clear project overview
├── .gitignore                        # ✅ Created - Ignore data files, OS junk
├── requirements.txt                  # TODO - Python dependencies
├── pyproject.toml                    # TODO - Modern Python project config
├── setup.py                          # TODO - Package installation
│
├── src/                              # Application code (currently empty)
│   └── lawstronaut/
│       ├── __init__.py
│       ├── llm_client.py            # LLM API clients
│       ├── contract_analyzer.py     # Contract analysis logic
│       └── regulatory_retriever.py  # Regulatory knowledge retrieval
│
├── tests/                            # Test code
│   ├── __init__.py
│   ├── test_gemini_vertex.py        # MOVED from "TEST DATA"
│   ├── test_llm_apis.py             # TODO - Create base tester class
│   └── conftest.py                  # Pytest configuration
│
├── scripts/                          # Utility scripts
│   ├── ingest_cuad_data.py          # Data loading scripts
│   └── analyze_regulatory_gaps.py   # Analysis scripts
│
├── data/                             # Large data files (NOT in git)
│   ├── .gitkeep                     # Keep empty directory in git
│   ├── CUAD_v1.json                 # 40MB - ignored
│   ├── master_clauses.csv           # 3.8MB - ignored
│   ├── full_contract_pdf/           # 510 PDFs - ignored
│   ├── full_contract_txt/           # 510 text files - ignored
│   └── README.md                    # Instructions for downloading data
│
├── docs/                             # Documentation
│   ├── PROJECT_SUMMARY.md           # MOVED from TEST DATA
│   ├── LAWSTRONAUT_TEST_MATRIX.md   # Moved from root
│   ├── SUPABASE_SETUP.md            # Moved from root
│   ├── VERTEX_AI_APPLICATION_PROMPT.md  # MOVED from TEST DATA
│   └── questions.xlsx               # Renamed from "Lawstronaut questions.xlsx"
│
├── deploy/                           # Deployment configurations
│   ├── Dockerfile                   # MOVED from TEST DATA
│   ├── cloudbuild.yaml              # MOVED from TEST DATA
│   ├── setup-gcp.sh                 # MOVED from TEST DATA
│   └── README.md                    # Deployment instructions
│
└── notebooks/                        # Jupyter notebooks (if any)
    └── exploratory_analysis.ipynb
```

---

## Cleanup Steps

### Phase 1: Immediate Cleanup (Do Now)

1. **✅ Create .gitignore** - Stop tracking binary/data files
2. **✅ Create root README.md** - Clear project overview
3. **Remove junk from git**:
   ```bash
   git rm .DS_Store
   git rm ~$*.xlsx  # Excel lock files
   git rm --cached CUAD_v1.json master_clauses.csv  # Keep files, stop tracking
   git rm --cached -r full_contract_pdf/ full_contract_txt/ label_group_xlsx/
   ```

4. **Reorganize directories**:
   ```bash
   # Create new structure
   mkdir -p src/lawstronaut tests scripts docs deploy data

   # Move files
   mv "TEST DATA"/*.py tests/
   mv "TEST DATA"/*.md docs/
   mv "TEST DATA"/{Dockerfile,cloudbuild.yaml,setup-gcp.sh} deploy/
   mv LAWSTRONAUT_TEST_MATRIX.md SUPABASE_SETUP.md docs/
   mv "Lawstronaut questions.xlsx" docs/questions.xlsx

   # Move data files
   mv CUAD_v1.json master_clauses.csv data/
   mv full_contract_* data/
   mv label_group_xlsx data/
   mv CUAD_v1_README.txt data/

   # Remove empty "TEST DATA" folder
   rmdir "TEST DATA"
   ```

### Phase 2: Fix Python Project Structure

5. **Create requirements.txt**:
   ```txt
   google-genai>=1.0.0
   pandas>=2.0.0
   python-dotenv>=1.0.0
   openai>=1.0.0
   anthropic>=0.18.0
   supabase>=2.0.0
   ```

6. **Create pyproject.toml**:
   ```toml
   [build-system]
   requires = ["setuptools>=61.0", "wheel"]
   build-backend = "setuptools.build_meta"

   [project]
   name = "lawstronaut-cuad"
   version = "0.1.0"
   description = "Legal contract intelligence using LLMs with post-cutoff regulatory retrieval"
   readme = "README.md"
   requires-python = ">=3.10"
   dependencies = [
       "google-genai>=1.0.0",
       "pandas>=2.0.0",
       "python-dotenv>=1.0.0",
   ]
   ```

7. **Create src/lawstronaut package structure**:
   ```bash
   touch src/lawstronaut/__init__.py
   ```

8. **Fix test imports**:
   - Create `tests/test_llm_apis.py` with `LawstronautTester` base class
   - Fix imports in `test_gemini_vertex.py`

### Phase 3: Data Management

9. **Create data/README.md** with download instructions
10. **Consider Git LFS** for versioning large files (if needed)
11. **Or use external storage** (Google Drive, S3, etc.)

### Phase 4: Documentation

12. **Consolidate docs**:
    - ✅ Root README.md created
    - Move verbose docs to docs/
    - Create deploy/README.md for GCP setup
    - Create data/README.md for dataset instructions

### Phase 5: Decide Project Direction

13. **Choose one of these paths**:

    **Option A: Research Project**
    - Focus on LLM testing and evaluation
    - Keep test scripts as main deliverable
    - Publish findings/benchmarks
    - Remove incomplete Supabase/deployment code

    **Option B: Production Tool**
    - Implement proper application in src/
    - Complete backend (Supabase or alternative)
    - Build REST API
    - Deploy to GCP
    - Significant development required

14. **Remove or complete half-finished features**:
    - Either implement Supabase backend or remove SUPABASE_SETUP.md
    - Either complete GCP deployment or remove deploy/
    - Don't leave documentation for non-existent features

---

## Git Commands for Cleanup

```bash
# Stage initial cleanup files
git add .gitignore README.md CLEANUP_PLAN.md

# Remove junk
git rm .DS_Store
git rm '~$Lawstronaut questions.xlsx'

# Stop tracking large data files (keep locally)
git rm --cached CUAD_v1.json
git rm --cached master_clauses.csv
git rm --cached -r full_contract_pdf/
git rm --cached -r full_contract_txt/
git rm --cached -r label_group_xlsx/

# Commit cleanup
git commit -m "Initial cleanup: Add .gitignore, README, remove data files from git"

# Create new directory structure (do this manually first, then commit)
# git add -A
# git commit -m "Reorganize: Move files to proper directory structure"
```

---

## Recommendations

### Critical Issues to Address

1. **Decide on project scope** - Research or production?
2. **Remove incomplete features** - Don't document things that don't exist
3. **Fix Python imports** - Create proper package structure
4. **Data management** - Get 270MB of files out of git history (may need force push)

### Nice to Have

1. CI/CD pipeline (GitHub Actions)
2. Pre-commit hooks (black, flake8, mypy)
3. Unit tests
4. API documentation
5. Docker compose for local development

### What to Delete

Consider removing if not actively working on:
- **SUPABASE_SETUP.md** (892 lines for non-existent backend)
- **GCP deployment files** (if not deploying)
- **Test matrix verbosity** (893 lines could be condensed)

### Priority Order

1. ✅ .gitignore + README (DONE)
2. Remove data files from git tracking
3. Reorganize directory structure
4. Create requirements.txt
5. Fix Python package structure
6. Decide project direction
7. Remove incomplete/unused code

---

## Questions to Answer

Before proceeding with full reorganization:

1. **What is the primary goal?**
   - [ ] Research/benchmarking LLMs for legal analysis
   - [ ] Build production legal intelligence tool
   - [ ] Dataset analysis and exploration

2. **What features are actually being developed?**
   - [ ] Gemini testing (active)
   - [ ] Supabase backend (only docs exist)
   - [ ] GCP deployment (incomplete)
   - [ ] Claude/GPT-4 comparison (incomplete)

3. **What should be removed?**
   - [ ] Supabase docs (if not implementing)
   - [ ] GCP deployment (if not deploying)
   - [ ] Incomplete test frameworks

4. **Data management approach?**
   - [ ] Keep data files locally, not in git (.gitignore)
   - [ ] Use Git LFS for versioning
   - [ ] External storage (Google Drive, S3)

---

## Next Actions

**Immediate (today):**
1. ✅ Review this cleanup plan
2. ✅ Commit .gitignore + README.md
3. Remove data files from git tracking
4. Create proper directory structure

**Short-term (this week):**
1. Fix Python package structure
2. Create requirements.txt
3. Move files to new locations
4. Decide project direction

**Medium-term:**
1. Complete test suite OR remove incomplete code
2. Implement backend OR remove architecture docs
3. Deploy to GCP OR remove deployment configs
4. Focus on one clear deliverable

---

**Status**: Cleanup started, directory structure planned, project direction TBD
