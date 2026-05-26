# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

AI Engineer learning workspace. Each directory maps to a phase in `ai-engineer-study-map.md`. All dirs are currently empty stubs — code gets added as phases are completed.

## Directory → Phase Mapping

| Dir | Phase | Focus |
|-----|-------|-------|
| `python/` | 1 (Weeks 1-3) | Advanced Python, FastAPI, async, Postgres |
| `llm-api/` | 2 (Weeks 4-5) | OpenAI SDK, Anthropic SDK, prompt engineering |
| `rag/` | 3 (Weeks 6-8) | Embeddings, pgvector/Pinecone, RAG pipelines, evals |
| `orchestration/` | 4 (Weeks 9-10) | LangChain LCEL, LangGraph |
| `mpc/` | 5 (Week 11) | Model Context Protocol |
| `eval-observability/` | 6 (Week 12) | LangSmith, LLM-as-judge, Ragas |
| `cloud/` | 7 (Weeks 13-14) | Docker, AWS, Modal, Railway, GitHub Actions |

## Conventions (from study map)

- Use `uv` for Python package management (not pip/poetry)
- Ruff for linting/formatting, mypy for type checking (`mypy --strict` goal)
- 100% type hints on all new code
- Structured logging instead of `print()`
- pytest for tests; cover the main flow at minimum
- Pydantic v2 for data models

## Key Stack

Python-first. Likely dependencies per phase:
- **llm-api**: `anthropic`, `openai`, `tiktoken`
- **rag**: `pgvector`, `pinecone-client`, `ragas`, `sentence-transformers`
- **orchestration**: `langchain`, `langgraph`
- **eval-observability**: `langsmith`
- **cloud**: Docker, AWS CDK or boto3, `modal`

## Study Map Reference

`ai-engineer-study-map.md` — full roadmap with resources, domain checks, and anti-patterns per phase. Read this before scaffolding any new phase directory.
