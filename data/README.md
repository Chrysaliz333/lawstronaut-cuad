# CUAD Dataset - Legal Contracts

This directory contains the Contract Understanding Atticus Dataset (CUAD) v1.

## Large Data Files (Not in Git)

The following files are **NOT tracked in git** due to their size (270MB+ total):

```
data/
├── CUAD_v1.json (40MB) - SQuAD format dataset
├── master_clauses.csv (3.8MB) - Contract metadata and clause labels
├── full_contract_pdf/ (~200MB) - 510 PDF contracts
├── full_contract_txt/ (26MB) - 510 text contracts
└── label_group_xlsx/ - CUAD clause label groups
```

## How to Get the Data

### Option 1: Download from CUAD Repository

```bash
# Clone the original CUAD repository
git clone https://github.com/TheAtticusProject/cuad.git /tmp/cuad

# Copy data files to this project
cp /tmp/cuad/data/CUAD_v1.json data/
cp /tmp/cuad/data/master_clauses.csv data/
cp -r /tmp/cuad/data/full_contract_pdf data/
cp -r /tmp/cuad/data/full_contract_txt data/
cp -r /tmp/cuad/data/label_group_xlsx data/
```

### Option 2: Download Individual Files

If you already have the CUAD data elsewhere, simply copy/move the files to this `data/` directory.

## Data Structure

### CUAD_v1.json
- SQuAD 2.0 format
- 510 contracts with question-answer pairs
- 41 legal clause categories

### master_clauses.csv
- One row per contract
- Columns for each of 41 clause types
- Metadata: parties, dates, governing law

### full_contract_txt/
- Plain text versions of all contracts
- Used for testing LLM analysis

### full_contract_pdf/
- Original PDF contracts
- Organized by contract type subdirectories

## CUAD Dataset License

The CUAD dataset is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).

Original dataset: https://github.com/TheAtticusProject/cuad

## References

For more information about the CUAD dataset, see:
- `CUAD_v1_README.txt` (original dataset documentation)
- https://www.atticusprojectai.org/cuad
