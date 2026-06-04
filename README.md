# AI Engineer

Learning workspace for becoming a production AI Engineer. Built around a 14-week study map (~210h) covering the full stack: Python → LLM APIs → RAG → Agents → MCP → Evals → Cloud.

## Structure

Each directory is an independent `uv` project for one phase:

| Dir | Phase | Focus |
|-----|-------|-------|
| `python/` | 1 (Weeks 1-3) | Advanced Python, FastAPI, async, Postgres |
| `llm-api/` | 2 (Weeks 4-5) | OpenAI + Anthropic SDKs, prompt engineering |
| `rag/` | 3 (Weeks 6-8) | Embeddings, pgvector/Pinecone, hybrid search, evals |
| `orchestration/` | 4 (Weeks 9-10) | LangChain LCEL, LangGraph |
| `mpc/` | 5 (Week 11) | Model Context Protocol |
| `eval-observability/` | 6 (Week 12) | LangSmith, LLM-as-judge, Ragas |
| `cloud/` | 7 (Weeks 13-14) | Docker, AWS Lambda, Modal, GitHub Actions |
| `agents/` | — | Standalone agent experiments |

## Stack

- **Runtime**: Python 3.12+, `uv` for package management
- **Quality**: Ruff (lint/format), mypy (`--strict` goal), pytest
- **LLMs**: OpenAI, Anthropic Claude
- **Vector**: pgvector, Pinecone, FAISS
- **Orchestration**: LangChain, LangGraph
- **Deploy**: Docker, AWS, Modal

## Dev workflow

```bash
# Scaffold a new phase
uv init <phase-dir>
cd <phase-dir>
uv add --dev pytest ruff mypy

# Run tests / lint / types
uv run pytest
uv run pytest tests/test_foo.py -k "test_name"
uv run ruff check . && uv run ruff format .
uv run mypy src/
```

## Roadmap

Full study map with resources, domain checks, and anti-patterns: [`ai-engineer-study-map.md`](ai-engineer-study-map.md)
