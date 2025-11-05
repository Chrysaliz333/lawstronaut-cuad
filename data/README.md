# Test Contracts for Lawstronaut

This directory contains the specific legal contracts used for testing Gemini with Vertex AI.

## Test Contracts (Small - Already Included)

You **only need 5 contracts** for the 6 test questions (Q1A and Q1B share one contract):

```
data/test_contracts/
├── FOUNDATIONMEDICINE,INC_02_02_2015-EX-10.2-Collaboration Agreement.txt
├── WPPPLC_04_30_2020-EX-4.28-SERVICE AGREEMENT.txt
├── CardlyticsInc_20180112_S-1_EX-10.16_11002987_EX-10.16_Maintenance Agreement1.txt
├── UpjohnInc_20200121_10-12G_EX-2.6_11948692_EX-2.6_Manufacturing Agreement_ Supply Agreement.txt
└── MEDALISTDIVERSIFIEDREIT,INC_05_18_2020-EX-10.1-CONSULTING AGREEMENT.txt
```

**Total size:** ~650KB (not 270MB!)

## Quick Setup

If the test contracts aren't already in `data/test_contracts/`, run:

```bash
# From project root
./scripts/setup_test_contracts.sh
```

This extracts just the 5 needed contracts from the full CUAD dataset.

## Test Questions Mapping

- **Q1A** (Data Processing) → Foundation Medicine contract
- **Q1B** (Data Governance) → Foundation Medicine contract (same file)
- **Q2A** (Brexit) → WPP PLC contract
- **Q3A** (California Data) → Cardlytics contract
- **Q4A** (ESG) → Upjohn contract
- **Q5A** (Non-Compete) → Medalist Diversified contract

## Full CUAD Dataset (Optional)

If you need the complete dataset (510 contracts, 270MB):

```bash
# Clone the original CUAD repository
git clone https://github.com/TheAtticusProject/cuad.git /tmp/cuad

# Copy full dataset
cp -r /tmp/cuad/data/full_contract_txt ../
cp /tmp/cuad/data/CUAD_v1.json data/
cp /tmp/cuad/data/master_clauses.csv data/
```

### CUAD Dataset Structure

- **CUAD_v1.json** - SQuAD 2.0 format, 510 contracts with Q&A pairs
- **master_clauses.csv** - Contract metadata and 41 clause types
- **full_contract_txt/** - Plain text versions of all 510 contracts
- **full_contract_pdf/** - Original PDF contracts

## License

The CUAD dataset is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).

- Original dataset: https://github.com/TheAtticusProject/cuad
- More info: https://www.atticusprojectai.org/cuad
- Documentation: `CUAD_v1_README.txt`
