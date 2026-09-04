# ORCA v2 — Agentic Retail Replenishment on Google Cloud

Production-grade agentic AI for retail inventory replenishment, with a
deterministic capital-commitment gate and human-in-the-loop approval.

**Status:** Week 1 — agentic core

## Why v2

[ORCA v1](https://github.com/ankitv42/orca-retail) proved the concept but had
architectural gaps: a linear pipeline described as multi-agent, MCP over stdio,
no authentication, no document ingestion pipeline, no cost accounting, no
guardrails.

v2 is a ground-up rebuild addressing each of those, designed GCP-native.

## Design principles

1. **Agentic where reasoning helps, deterministic where money moves.**
   The agent recommends. Pure Python decides whether to commit capital.
2. **Domain logic has no infrastructure dependencies.** Scoring and routing
   are unit-testable without a database, an API key, or a network.
3. **Every external dependency sits behind an interface.** Storage and LLM
   providers swap by configuration, not by code change.
4. **Cost is a first-class metric,** measured per decision from Week 1.

## Stack

| Layer | Technology |
|---|---|
| Orchestration | LangGraph |
| LLM | Gemini (AI Studio → Vertex) |
| Storage | SQLite → Firestore |
| API | FastAPI on Cloud Run |
| Dashboard | Streamlit on Cloud Run |
| IaC | Terraform |

## Architecture Decision Records

See [`docs/adr/`](docs/adr/).

## Local development

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env   # then fill in GOOGLE_API_KEY
python scripts\check_config.py
```

---
Built by **Ankit Kumar Verma** — Data Science Manager, Accenture