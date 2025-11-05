# Supabase Backend Setup for Lawstronaut CUAD Project

This guide sets up a comprehensive backend for your legal contract analysis LLM system using Supabase with pgvector for semantic search.

## Overview

Your Lawstronaut project analyzes 510 contracts from the CUAD dataset for regulatory compliance. This backend will provide:

1. **Contract Storage** - Metadata and full text for 510 contracts
2. **Vector Search** - Semantic search across contracts using embeddings
3. **Regulatory Tracking** - Store and query regulatory changes (EU AI Act, FTC rules, etc.)
4. **Analysis Results** - Store LLM analysis results and compliance gaps
5. **Test Questions** - Manage your test matrix for evaluating Lawstronaut
6. **User Management** - Track users and their queries

## Quick Start

```bash
cd ~/Projects/AI-ML/Contract-Intelligence/lawstronaut-cuad
supabase init
supabase start
```

## Database Schema

### 1. Create Migration

```bash
supabase migration new lawstronaut_schema
```

Edit the migration file in `supabase/migrations/`:

```sql
-- Enable extensions
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ======================
-- CONTRACTS
-- ======================

CREATE TABLE public.contracts (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  document_name TEXT UNIQUE NOT NULL,
  file_path_txt TEXT NOT NULL,
  file_path_pdf TEXT,

  -- Parties and metadata
  parties JSONB DEFAULT '[]'::jsonb,
  agreement_date DATE,
  effective_date DATE,
  expiration_date DATE,
  governing_law TEXT,

  -- Contract classification
  contract_type TEXT, -- 'License Agreement', 'Supply Agreement', etc.
  industry_sector TEXT, -- 'Pharmaceuticals', 'Technology', etc.

  -- Full text
  full_text TEXT,
  full_text_length INTEGER,

  -- CUAD master_clauses.csv data
  cuad_row_data JSONB DEFAULT '{}'::jsonb,

  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ======================
-- CLAUSES (41 CUAD categories)
-- ======================

CREATE TABLE public.clauses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  contract_id UUID REFERENCES public.contracts(id) ON DELETE CASCADE,

  -- Clause identification
  clause_category TEXT NOT NULL, -- One of 41 CUAD categories
  clause_group INTEGER, -- Group 1-5 or NULL (from CUAD taxonomy)

  -- Clause content
  context TEXT, -- The full clause text
  answer TEXT, -- Derived answer (e.g., 'Yes/No', date, entity name)
  answer_type TEXT, -- 'yes_no', 'date', 'entity', 'duration'

  -- Location in contract
  paragraph_reference TEXT,
  page_number INTEGER,

  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for fast clause lookup
CREATE INDEX idx_clauses_contract ON public.clauses(contract_id);
CREATE INDEX idx_clauses_category ON public.clauses(clause_category);

-- ======================
-- EMBEDDINGS (Vector Search)
-- ======================

CREATE TABLE public.contract_embeddings (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  contract_id UUID REFERENCES public.contracts(id) ON DELETE CASCADE,

  -- Chunk information
  chunk_index INTEGER NOT NULL,
  chunk_text TEXT NOT NULL,
  chunk_length INTEGER,

  -- Vector embedding
  embedding vector(1536), -- OpenAI text-embedding-3-small dimension

  -- Metadata
  metadata JSONB DEFAULT '{}'::jsonb,

  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Vector similarity search index
CREATE INDEX idx_embeddings_vector ON public.contract_embeddings
USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);

CREATE INDEX idx_embeddings_contract ON public.contract_embeddings(contract_id);

-- ======================
-- REGULATIONS (Post-cutoff regulatory changes)
-- ======================

CREATE TABLE public.regulations (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

  -- Regulation identification
  regulation_name TEXT NOT NULL,
  regulation_type TEXT, -- 'EU AI Act', 'FTC Non-Compete Ban', 'State AI Law', etc.
  jurisdiction TEXT, -- 'EU', 'US Federal', 'California', 'UK', etc.

  -- Key dates
  proposed_date DATE,
  enacted_date DATE,
  effective_date DATE,
  enforcement_start DATE,

  -- Content
  summary TEXT,
  key_provisions JSONB DEFAULT '[]'::jsonb,
  affected_industries TEXT[],

  -- Status
  status TEXT, -- 'proposed', 'enacted', 'in_force', 'blocked', 'amended'
  current_status_detail TEXT,

  -- References
  official_citation TEXT,
  url TEXT,

  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for regulation lookup
CREATE INDEX idx_regulations_type ON public.regulations(regulation_type);
CREATE INDEX idx_regulations_jurisdiction ON public.regulations(jurisdiction);
CREATE INDEX idx_regulations_effective_date ON public.regulations(effective_date DESC);

-- ======================
-- REGULATORY EXPOSURE (Which contracts are affected by which regulations)
-- ======================

CREATE TABLE public.regulatory_exposure (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  contract_id UUID REFERENCES public.contracts(id) ON DELETE CASCADE,
  regulation_id UUID REFERENCES public.regulations(id) ON DELETE CASCADE,

  -- Exposure assessment
  risk_level TEXT, -- 'critical', 'high', 'medium', 'low'
  applicability_confidence TEXT, -- 'high', 'medium', 'low'

  -- Analysis
  affected_provisions JSONB DEFAULT '[]'::jsonb,
  compliance_gaps JSONB DEFAULT '[]'::jsonb,
  recommended_actions TEXT,

  -- Timestamps
  assessed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  last_reviewed TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  UNIQUE(contract_id, regulation_id)
);

-- Index for exposure lookup
CREATE INDEX idx_exposure_contract ON public.regulatory_exposure(contract_id);
CREATE INDEX idx_exposure_regulation ON public.regulatory_exposure(regulation_id);
CREATE INDEX idx_exposure_risk ON public.regulatory_exposure(risk_level);

-- ======================
-- TEST QUESTIONS (Your test matrix)
-- ======================

CREATE TABLE public.test_questions (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

  -- Question identification
  question_id TEXT UNIQUE NOT NULL,
  category TEXT NOT NULL, -- 'EU AI Act', 'UK REUL', 'US State AI', etc.

  -- Associated contract
  contract_id UUID REFERENCES public.contracts(id),

  -- Question content
  question_text TEXT NOT NULL,
  expected_answer_type TEXT, -- 'compliance_analysis', 'gap_identification', 'regulation_retrieval'

  -- Ground truth (if available)
  ground_truth_answer TEXT,
  key_facts JSONB DEFAULT '[]'::jsonb,

  -- Testing metadata
  difficulty TEXT, -- 'baseline', 'complex', 'multi-regulatory'
  test_phase TEXT, -- 'phase_1', 'phase_2', 'phase_3', 'phase_4'
  priority INTEGER DEFAULT 0,

  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for test questions
CREATE INDEX idx_test_questions_category ON public.test_questions(category);
CREATE INDEX idx_test_questions_contract ON public.test_questions(contract_id);
CREATE INDEX idx_test_questions_priority ON public.test_questions(priority DESC);

-- ======================
-- LLM RESPONSES (Store Lawstronaut vs baseline LLM responses)
-- ======================

CREATE TABLE public.llm_responses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  test_question_id UUID REFERENCES public.test_questions(id) ON DELETE CASCADE,

  -- Model information
  model_type TEXT NOT NULL, -- 'lawstronaut', 'baseline_gpt4', 'baseline_claude'
  model_version TEXT,

  -- Response
  response_text TEXT NOT NULL,
  tokens_used INTEGER,
  latency_ms INTEGER,

  -- Retrieved regulations (for Lawstronaut)
  regulations_retrieved JSONB DEFAULT '[]'::jsonb,

  -- Evaluation
  correctness_score NUMERIC, -- 0-1
  completeness_score NUMERIC, -- 0-1
  retrieval_accuracy NUMERIC, -- 0-1 (for regulations)
  evaluator_notes TEXT,

  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for responses
CREATE INDEX idx_responses_question ON public.llm_responses(test_question_id);
CREATE INDEX idx_responses_model ON public.llm_responses(model_type);

-- ======================
-- USER QUERIES (Track real usage)
-- ======================

CREATE TABLE public.user_queries (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users(id),

  -- Query
  query_text TEXT NOT NULL,
  query_type TEXT, -- 'semantic_search', 'compliance_check', 'regulation_lookup'

  -- Context
  contract_ids UUID[], -- Contracts being queried
  regulation_ids UUID[], -- Regulations being checked

  -- Response
  response_text TEXT,
  response_time_ms INTEGER,

  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for user queries
CREATE INDEX idx_user_queries_user ON public.user_queries(user_id);
CREATE INDEX idx_user_queries_created ON public.user_queries(created_at DESC);

-- ======================
-- PROFILES (User management)
-- ======================

CREATE TABLE public.profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email TEXT UNIQUE NOT NULL,
  full_name TEXT,
  organization TEXT,
  role TEXT DEFAULT 'analyst', -- 'analyst', 'admin', 'researcher'
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ======================
-- ROW LEVEL SECURITY
-- ======================

ALTER TABLE public.contracts ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.clauses ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.contract_embeddings ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.regulations ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.regulatory_exposure ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.test_questions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.llm_responses ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_queries ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

-- Public read access to contracts and regulations (or customize as needed)
CREATE POLICY "Contracts are viewable by authenticated users"
  ON public.contracts FOR SELECT
  TO authenticated
  USING (true);

CREATE POLICY "Regulations are viewable by authenticated users"
  ON public.regulations FOR SELECT
  TO authenticated
  USING (true);

-- Users can view their own queries
CREATE POLICY "Users can view own queries"
  ON public.user_queries FOR SELECT
  USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own queries"
  ON public.user_queries FOR INSERT
  WITH CHECK (auth.uid() = user_id);

-- Users can view their own profile
CREATE POLICY "Users can view own profile"
  ON public.profiles FOR SELECT
  USING (auth.uid() = id);

-- ======================
-- FUNCTIONS
-- ======================

-- Semantic search function
CREATE OR REPLACE FUNCTION match_contracts(
  query_embedding vector(1536),
  match_threshold float DEFAULT 0.7,
  match_count int DEFAULT 10
)
RETURNS TABLE (
  contract_id uuid,
  chunk_text text,
  similarity float,
  contract_name text,
  governing_law text
)
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  SELECT
    ce.contract_id,
    ce.chunk_text,
    1 - (ce.embedding <=> query_embedding) AS similarity,
    c.document_name,
    c.governing_law
  FROM public.contract_embeddings ce
  JOIN public.contracts c ON c.id = ce.contract_id
  WHERE 1 - (ce.embedding <=> query_embedding) > match_threshold
  ORDER BY ce.embedding <=> query_embedding
  LIMIT match_count;
END;
$$;

-- Get compliance dashboard for a contract
CREATE OR REPLACE FUNCTION get_contract_compliance_dashboard(p_contract_id uuid)
RETURNS TABLE (
  contract_name text,
  total_regulations int,
  critical_risks int,
  high_risks int,
  medium_risks int,
  low_risks int,
  regulations json
)
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  SELECT
    c.document_name,
    COUNT(DISTINCT re.regulation_id)::int AS total_regulations,
    COUNT(DISTINCT CASE WHEN re.risk_level = 'critical' THEN re.regulation_id END)::int AS critical_risks,
    COUNT(DISTINCT CASE WHEN re.risk_level = 'high' THEN re.regulation_id END)::int AS high_risks,
    COUNT(DISTINCT CASE WHEN re.risk_level = 'medium' THEN re.regulation_id END)::int AS medium_risks,
    COUNT(DISTINCT CASE WHEN re.risk_level = 'low' THEN re.regulation_id END)::int AS low_risks,
    json_agg(
      json_build_object(
        'regulation_name', r.regulation_name,
        'risk_level', re.risk_level,
        'compliance_gaps', re.compliance_gaps
      )
    ) AS regulations
  FROM public.contracts c
  LEFT JOIN public.regulatory_exposure re ON re.contract_id = c.id
  LEFT JOIN public.regulations r ON r.id = re.regulation_id
  WHERE c.id = p_contract_id
  GROUP BY c.document_name;
END;
$$;

-- Get contracts affected by a specific regulation
CREATE OR REPLACE FUNCTION get_contracts_by_regulation(
  p_regulation_id uuid,
  p_min_risk_level text DEFAULT 'low'
)
RETURNS TABLE (
  contract_id uuid,
  contract_name text,
  risk_level text,
  compliance_gaps jsonb
)
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  SELECT
    c.id,
    c.document_name,
    re.risk_level,
    re.compliance_gaps
  FROM public.contracts c
  JOIN public.regulatory_exposure re ON re.contract_id = c.id
  WHERE re.regulation_id = p_regulation_id
    AND (
      CASE p_min_risk_level
        WHEN 'critical' THEN re.risk_level = 'critical'
        WHEN 'high' THEN re.risk_level IN ('critical', 'high')
        WHEN 'medium' THEN re.risk_level IN ('critical', 'high', 'medium')
        ELSE true
      END
    )
  ORDER BY
    CASE re.risk_level
      WHEN 'critical' THEN 1
      WHEN 'high' THEN 2
      WHEN 'medium' THEN 3
      WHEN 'low' THEN 4
    END;
END;
$$;

-- Update timestamp trigger
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_contracts_updated_at
  BEFORE UPDATE ON public.contracts
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER update_regulations_updated_at
  BEFORE UPDATE ON public.regulations
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();
```

### 2. Apply Migration

```bash
supabase db reset
```

## Python Integration

### Install Dependencies

```bash
pip install supabase openai pandas python-dotenv
```

### Environment Variables

Add to `.env`:

```bash
# Supabase
SUPABASE_URL=http://localhost:54321
SUPABASE_KEY=your-anon-key-here

# OpenAI (for embeddings)
OPENAI_API_KEY=your-openai-key-here
```

### Python Client

Create `lawstronaut_backend.py`:

```python
from supabase import create_client, Client
from openai import OpenAI
import os
import pandas as pd
from typing import List, Dict, Optional
import json

class LawstronautBackend:
    def __init__(self):
        self.supabase = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )
        self.openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # ====================
    # CONTRACT INGESTION
    # ====================

    def ingest_contract(
        self,
        document_name: str,
        file_path_txt: str,
        full_text: str,
        metadata: Dict
    ) -> Dict:
        """Ingest a contract into the database"""
        data = {
            "document_name": document_name,
            "file_path_txt": file_path_txt,
            "full_text": full_text,
            "full_text_length": len(full_text),
            **metadata
        }

        result = self.supabase.table("contracts").insert(data).execute()
        return result.data[0]

    def ingest_clause(
        self,
        contract_id: str,
        clause_category: str,
        context: str,
        answer: str,
        answer_type: str,
        clause_group: Optional[int] = None
    ) -> Dict:
        """Ingest a clause from CUAD dataset"""
        data = {
            "contract_id": contract_id,
            "clause_category": clause_category,
            "context": context,
            "answer": answer,
            "answer_type": answer_type,
            "clause_group": clause_group
        }

        result = self.supabase.table("clauses").insert(data).execute()
        return result.data[0]

    def generate_and_store_embedding(
        self,
        contract_id: str,
        chunk_text: str,
        chunk_index: int
    ) -> Dict:
        """Generate embedding and store in database"""
        # Generate embedding using OpenAI
        response = self.openai.embeddings.create(
            model="text-embedding-3-small",
            input=chunk_text
        )
        embedding = response.data[0].embedding

        # Store in database
        data = {
            "contract_id": contract_id,
            "chunk_index": chunk_index,
            "chunk_text": chunk_text,
            "chunk_length": len(chunk_text),
            "embedding": embedding
        }

        result = self.supabase.table("contract_embeddings").insert(data).execute()
        return result.data[0]

    # ====================
    # SEMANTIC SEARCH
    # ====================

    def semantic_search(
        self,
        query: str,
        match_threshold: float = 0.7,
        match_count: int = 10
    ) -> List[Dict]:
        """Perform semantic search across contracts"""
        # Generate query embedding
        response = self.openai.embeddings.create(
            model="text-embedding-3-small",
            input=query
        )
        query_embedding = response.data[0].embedding

        # Search database
        result = self.supabase.rpc(
            "match_contracts",
            {
                "query_embedding": query_embedding,
                "match_threshold": match_threshold,
                "match_count": match_count
            }
        ).execute()

        return result.data

    # ====================
    # REGULATORY MANAGEMENT
    # ====================

    def add_regulation(
        self,
        regulation_name: str,
        regulation_type: str,
        jurisdiction: str,
        effective_date: str,
        summary: str,
        status: str = "in_force"
    ) -> Dict:
        """Add a post-cutoff regulation"""
        data = {
            "regulation_name": regulation_name,
            "regulation_type": regulation_type,
            "jurisdiction": jurisdiction,
            "effective_date": effective_date,
            "summary": summary,
            "status": status
        }

        result = self.supabase.table("regulations").insert(data).execute()
        return result.data[0]

    def link_contract_to_regulation(
        self,
        contract_id: str,
        regulation_id: str,
        risk_level: str,
        compliance_gaps: List[str]
    ) -> Dict:
        """Link a contract to a regulation with risk assessment"""
        data = {
            "contract_id": contract_id,
            "regulation_id": regulation_id,
            "risk_level": risk_level,
            "compliance_gaps": json.dumps(compliance_gaps)
        }

        result = self.supabase.table("regulatory_exposure").upsert(data).execute()
        return result.data[0]

    # ====================
    # COMPLIANCE DASHBOARD
    # ====================

    def get_contract_compliance(self, contract_id: str) -> Dict:
        """Get compliance dashboard for a contract"""
        result = self.supabase.rpc(
            "get_contract_compliance_dashboard",
            {"p_contract_id": contract_id}
        ).execute()

        return result.data[0] if result.data else None

    def get_high_risk_contracts(self) -> List[Dict]:
        """Get all contracts with critical or high regulatory risks"""
        result = self.supabase.table("regulatory_exposure")\
            .select("*, contracts(*), regulations(*)")\
            .in_("risk_level", ["critical", "high"])\
            .execute()

        return result.data

    # ====================
    # TEST MANAGEMENT
    # ====================

    def add_test_question(
        self,
        question_id: str,
        category: str,
        question_text: str,
        contract_id: Optional[str] = None,
        priority: int = 0
    ) -> Dict:
        """Add a test question from your test matrix"""
        data = {
            "question_id": question_id,
            "category": category,
            "question_text": question_text,
            "contract_id": contract_id,
            "priority": priority
        }

        result = self.supabase.table("test_questions").insert(data).execute()
        return result.data[0]

    def save_llm_response(
        self,
        test_question_id: str,
        model_type: str,
        response_text: str,
        tokens_used: int,
        latency_ms: int,
        regulations_retrieved: Optional[List[str]] = None
    ) -> Dict:
        """Save an LLM response for comparison"""
        data = {
            "test_question_id": test_question_id,
            "model_type": model_type,
            "response_text": response_text,
            "tokens_used": tokens_used,
            "latency_ms": latency_ms,
            "regulations_retrieved": json.dumps(regulations_retrieved or [])
        }

        result = self.supabase.table("llm_responses").insert(data).execute()
        return result.data[0]

    # ====================
    # BULK OPERATIONS
    # ====================

    def bulk_ingest_from_csv(self, csv_path: str):
        """Bulk ingest from CUAD master_clauses.csv"""
        df = pd.read_csv(csv_path)

        for idx, row in df.iterrows():
            # Extract contract metadata
            document_name = row.iloc[0]  # First column is document name

            # Read full text
            txt_path = f"full_contract_txt/{document_name}.txt"
            if os.path.exists(txt_path):
                with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
                    full_text = f.read()
            else:
                full_text = ""

            # Ingest contract
            contract = self.ingest_contract(
                document_name=document_name,
                file_path_txt=txt_path,
                full_text=full_text,
                metadata={}
            )

            print(f"Ingested: {document_name}")

# Example usage
if __name__ == "__main__":
    backend = LawstronautBackend()

    # Add a regulation
    eu_ai_act = backend.add_regulation(
        regulation_name="EU AI Act",
        regulation_type="AI Regulation",
        jurisdiction="EU",
        effective_date="2024-08-01",
        summary="Regulation 2024/1689 on AI systems",
        status="in_force"
    )

    # Semantic search
    results = backend.semantic_search(
        query="What contracts have algorithmic decision-making provisions?",
        match_count=5
    )

    for result in results:
        print(f"{result['contract_name']}: {result['similarity']:.2f}")
```

## Data Ingestion Script

Create `ingest_cuad_data.py`:

```python
#!/usr/bin/env python3
"""
Ingest CUAD dataset into Supabase
"""

from lawstronaut_backend import LawstronautBackend
import pandas as pd
import os
from pathlib import Path

def ingest_all_contracts():
    backend = LawstronautBackend()

    # Load master CSV
    csv_path = "master_clauses.csv"
    df = pd.read_csv(csv_path)

    print(f"Found {len(df)} contracts to ingest")

    for idx, row in df.iterrows():
        document_name = row.iloc[0]

        # Read full text
        txt_path = f"full_contract_txt/{document_name}.txt"

        if not os.path.exists(txt_path):
            print(f"Warning: {txt_path} not found, skipping...")
            continue

        with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
            full_text = f.read()

        # Ingest contract
        try:
            contract = backend.ingest_contract(
                document_name=document_name,
                file_path_txt=txt_path,
                full_text=full_text,
                metadata={
                    "cuad_row_data": row.to_dict()
                }
            )

            print(f"✓ Ingested: {document_name}")

            # Generate embeddings (chunk the text)
            chunk_size = 1000
            chunks = [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size)]

            for chunk_idx, chunk in enumerate(chunks):
                backend.generate_and_store_embedding(
                    contract_id=contract['id'],
                    chunk_text=chunk,
                    chunk_index=chunk_idx
                )

            print(f"  Generated {len(chunks)} embeddings")

        except Exception as e:
            print(f"✗ Error with {document_name}: {e}")

if __name__ == "__main__":
    ingest_all_contracts()
```

## Next Steps

1. **Start Supabase**:
   ```bash
   supabase start
   ```

2. **Apply schema**:
   ```bash
   supabase db reset
   ```

3. **Ingest your data**:
   ```bash
   python ingest_cuad_data.py
   ```

4. **Test semantic search**:
   ```python
   from lawstronaut_backend import LawstronautBackend
   backend = LawstronautBackend()
   results = backend.semantic_search("contracts with AI systems")
   ```

5. **Build your compliance tracker**!

## Resources

- Your test matrix: `LAWSTRONAUT_TEST_MATRIX.md`
- CUAD README: `CUAD_v1_README.txt`
- Contracts: `full_contract_txt/` (510 files)
- General backend guide: `~/Projects/BACKEND_SETUP_GUIDE.md`
