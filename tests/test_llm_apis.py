#!/usr/bin/env python3
"""
Base LLM tester class for Lawstronaut CUAD project
Provides common functionality for testing different LLM APIs
"""

import os
from pathlib import Path
from typing import Dict, Optional


class LawstronautTester:
    """Base class for testing LLM APIs with legal contract analysis."""

    def __init__(self, openai_key: Optional[str] = None, anthropic_key: Optional[str] = None):
        """
        Initialize the tester with API keys.

        Args:
            openai_key: OpenAI API key (optional)
            anthropic_key: Anthropic API key (optional)
        """
        self.openai_key = openai_key or os.getenv('OPENAI_API_KEY')
        self.anthropic_key = anthropic_key or os.getenv('ANTHROPIC_API_KEY')

        # Find contract data directory - try test_contracts first, fall back to full_contract_txt
        self.data_dir = Path(__file__).parent.parent / 'data' / 'test_contracts'
        if not self.data_dir.exists():
            # Fall back to full dataset if test_contracts doesn't exist
            self.data_dir = Path(__file__).parent.parent / 'full_contract_txt'

    def read_contract(self, contract_filename: str) -> str:
        """
        Read a contract text file from the data directory.

        Args:
            contract_filename: Name of the contract file (e.g., "FOUNDATIONMEDICINE...")

        Returns:
            Full contract text as string

        Raises:
            FileNotFoundError: If contract file doesn't exist
        """
        contract_path = self.data_dir / contract_filename

        if not contract_path.exists():
            # Try without .txt extension
            if not contract_filename.endswith('.txt'):
                contract_path = self.data_dir / f"{contract_filename}.txt"

        if not contract_path.exists():
            raise FileNotFoundError(
                f"Contract file not found: {contract_filename}\n"
                f"Looked in: {self.data_dir}"
            )

        with open(contract_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()

    def query_llm(self, contract_text: str, question: str, model: str = "gpt-4") -> Dict:
        """
        Query an LLM with a contract and question.

        Args:
            contract_text: Full contract text
            question: Legal question to ask
            model: Model identifier (e.g., "gpt-4", "claude-3", "gemini-pro")

        Returns:
            Dict containing response, model used, tokens, etc.
        """
        raise NotImplementedError("Subclasses must implement query_llm()")

    def test_question(self, contract_file: str, question_data: Dict) -> Dict:
        """
        Test a single question with a contract.

        Args:
            contract_file: Path to contract text file
            question_data: Dict with question text and metadata

        Returns:
            Dict containing test results
        """
        raise NotImplementedError("Subclasses must implement test_question()")


if __name__ == "__main__":
    print("This is a base class. Use test_gemini_vertex.py or similar to run tests.")
