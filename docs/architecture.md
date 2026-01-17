# AI Security Audit Copilot – Architecture

## Overview
The AI Security Audit Copilot is a modular AI system designed to assist (not replace)
security audits across smart contracts, application code, and security knowledge.

The system prioritizes correctness, transparency, and human oversight.

## High-Level Flow
1. User submits code or a question via the frontend
2. Request is sent to FastAPI backend
3. Relevant module is invoked
4. LLM reasoning is grounded using retrieval (RAG)
5. Guardrails validate confidence and output structure
6. Structured findings are returned to the user

## Core Components

### Frontend
- Next.js application
- Provides input interface and structured result display

### Backend (FastAPI)
- Orchestrates AI calls
- Enforces schemas and guardrails
- Exposes API endpoints per module

### LLM Layer
- Large Language Models used for reasoning
- Always constrained to structured outputs
- Never auto-approve security decisions

### RAG Layer
- Retrieves relevant security knowledge
- Provides citations and grounding
- Reduces hallucinations

### Guardrails
- Confidence thresholds
- Explicit "requires human review" flags
- Safety and scope constraints
