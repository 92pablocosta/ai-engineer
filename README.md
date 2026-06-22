# AI Engineer — Learning Journey

My path from LLM integrator to production AI/backend engineer. This repo is a **learning log, not a portfolio of finished products** — it grows only with work I actually build, by hand.

## Why this repo looks the way it does

One rule drives everything here: **during learning, AI is off-limits.** I write the code by hand, hit the wall, read the traceback myself, and only *then* check against AI.

I already have the opposite experience — a portfolio built fast with AI, and near-zero retention. So this time the goal is depth I can **defend live in an interview**: "how would you do this without LangChain?", "cosine or dot product, and why?", "what is HNSW?". AI stays my production tool; it just steps aside while I learn the fundamentals.

That means: **no empty scaffolding, no placeholder projects.** A phase directory appears here only when I start that phase. If a folder exists, there's real work in it.

## Roadmap & progress

Foundation is identical regardless of the final track. Phase folders sit at the repo root.

| Phase | Folder | Focus | Deliverable | Status |
|-------|--------|-------|-------------|--------|
| 0 | `00-python/` | OOP, type hints (`mypy`), `async`/`await` | OOP CLI script that calls the OpenAI API (intent classifier), hand-typed | Not started |
| 1 | `01-pytest/` | `pytest` from zero: fixtures, parametrize, API mocking | Green suite over the phase-0 script, incl. LLM mock | Not started |
| 2 | `02-fastapi/` | async routes, Pydantic v2, DI, middleware, errors | LLM endpoint (e.g. `/chat` streaming), tested + dockerized | Not started |
| 3 | `03-rag/` | embeddings + cosine in numpy → pgvector (IVFFlat/HNSW) → LangChain → LlamaIndex tour | RAG over my own docs, pgvector retrieval, served via FastAPI | Not started |
| 4 | `04-evals-observability/` | Langfuse (self-hosted), ragas (faithfulness, context precision) | Langfuse dashboard + ragas report of a measured improvement | Not started |
| 5 | `05-docker-aws/` | multi-stage Dockerfile/compose by hand; S3, IAM, EC2 | A project above deployed via my own Docker + a real S3 bucket | Not started |

After the foundation, the focus is the **job track**: remote/international roles (USD). That means LLM system design, practical DSA, and take-home polish — folded into the foundation work rather than a separate directory.

Full reasoning, baselines, and per-phase detail: [`ai-engineer-roadmap.md`](ai-engineer-roadmap.md).

## Stack & conventions

- **Runtime**: Python 3.12+, [`uv`](https://github.com/astral-sh/uv) for package management (not pip/poetry)
- **Quality**: Ruff (lint + format), mypy (`--strict` goal), pytest
- **Style**: 100% type hints, Pydantic v2 for data models, structured logging over `print()`
- **LLMs**: Anthropic Claude, OpenAI
- **Data/vector**: PostgreSQL + pgvector
- **Deploy**: Docker, AWS (S3/IAM/EC2)

Each phase folder is an independent `uv` project:

```bash
uv init foundation/NN-name
cd foundation/NN-name
uv add --dev pytest ruff mypy

uv run pytest          # tests
uv run ruff check .    # lint
uv run ruff format .   # format
uv run mypy src/       # types
```

## Layout

```
.
├── ai-engineer-roadmap.md   # source of truth: full roadmap + baselines
├── roadmaps/                # condensed 2026 market intelligence (target niche)
├── 00-python/ … 05-docker-aws/   # foundation phases 0–5
└── _archive/                # earlier work from a previous roadmap
```
