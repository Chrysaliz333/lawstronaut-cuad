#!/bin/bash
# Extract only the 5 contracts needed for the 6 test questions
# (Q1A and Q1B use the same contract)

set -e

echo "Setting up test contracts..."

# Create test contracts directory
mkdir -p data/test_contracts

# List of required contracts for the 6 test questions
CONTRACTS=(
    "FOUNDATIONMEDICINE,INC_02_02_2015-EX-10.2-Collaboration Agreement.txt"
    "WPPPLC_04_30_2020-EX-4.28-SERVICE AGREEMENT.txt"
    "CardlyticsInc_20180112_S-1_EX-10.16_11002987_EX-10.16_Maintenance Agreement1.txt"
    "UpjohnInc_20200121_10-12G_EX-2.6_11948692_EX-2.6_Manufacturing Agreement_ Supply Agreement.txt"
    "MEDALISTDIVERSIFIEDREIT,INC_05_18_2020-EX-10.1-CONSULTING AGREEMENT.txt"
)

# Copy contracts from full_contract_txt to test_contracts
for contract in "${CONTRACTS[@]}"; do
    if [ -f "full_contract_txt/$contract" ]; then
        cp "full_contract_txt/$contract" "data/test_contracts/"
        echo "✓ Copied: $contract"
    else
        echo "✗ Missing: $contract"
    fi
done

echo ""
echo "Setup complete! 5 contracts copied to data/test_contracts/"
echo "These contracts cover all 6 test questions (Q1A and Q1B share one contract)."
