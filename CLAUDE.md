# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

AI Engineer learning workspace. A learning **log**, not a product portfolio. The repo proves skill through one spine project — **Atlas**, an AI knowledge assistant — that grows phase by phase (v0 → v5). Each phase maps to `ai-engineer-roadmap.md`. Never scaffold empty placeholder directories or projects.

**The differentiator is the commit history, not the final code.** Commit per phase with clear messages. A recruiter opens `git log` and sees CLI → tested → API → RAG → evaluated → deployed. That progression proves each layer was understood — no vibe coder can forge it.

## The learning rule (overrides convenience)

**During the foundation phases, AI writes no code for the user.** The user writes it by hand, hits errors, reads tracebacks, then checks against AI. When asked to "build" or "do" a foundation exercise, prefer to *guide, review, and unblock* — do not hand over finished solutions unless the user explicitly asks for the answer. AI is a production tool here, not a learning shortcut.

## Structure — one spine project

Atlas is a single `uv` project at the repo root. It does not get rebuilt per phase — each phase **extends** it. The same `atlas/` evolves; phases are commits, not directories.

```
ai-engineer/
├── README.md            ← the story: what Atlas is, how it evolved, what each phase proves
├── ai-engineer-roadmap.md
└── atlas/
    ├── src/
    ├── tests/
    ├── scripts/
    └── README.md        ← architecture + decisions
```

## Phase → Atlas version mapping

Each phase adds a layer to the same Atlas codebase.

| Phase | Atlas | Focus | Deliverable |
|-------|-------|-------|-------------|
| 0 | v0 — CLI | OOP, type hints, async/await, Big O basics (why dict/set O(1) vs list O(n)) | `python -m atlas` multi-turn chat in terminal, all hand-typed |
| 1 | v1 — tested | pytest: fixtures, parametrize, mock the LLM | green suite, coverage > 80% on core |
| 2 | v2 — API | async routes, Pydantic v2, DI, streaming/SSE | `POST /chat` running on uvicorn, Swagger, green suite |
| 3 | v3 — RAG | numpy cosine → pgvector (IVFFlat/HNSW) → LangChain → LlamaIndex tour | Atlas answers questions over your own docs |
| 4 | v4 — observable | Langfuse (self-hosted), ragas | Langfuse dashboard + versioned eval report |
| 5 | v5 — deployed | multi-stage Docker + compose by hand; S3, IAM, EC2 | Atlas live with public URL + S3 for ingested docs |

Phase 3 ordering is mandatory: by hand (numpy) → pgvector → only then LangChain → LlamaIndex tour. Do not start from the framework. The interview opens the hood.

Not in scope on purpose: managed vector DBs (Pinecone/Qdrant/Weaviate) — pgvector covers it. Fine-tuning / model training — the focus is *applying* LLMs. MCP and LangGraph are not in the current roadmap.

## After the foundation — the fork

The foundation above serves both tracks. Decide direction only after finishing it:

- **Track EMPLOYMENT** (remote international, USD): LLM system design (caching, fallback, rate limit, eval gate, multi-tenancy), practical DSA (~30–40 Easy/Medium, NeetCode 150 lite), Big O analysis in depth (compute your own solution's complexity, optimize O(n²) → O(n) — the standard interview follow-up), take-home polish (small + complete > ambitious + broken).
- **Track BUILDER** (freela/agency/SaaS): deep deployment (CI/CD, monitoring, billing), productize Atlas as a replicable template, position as fast-delivery AI automation specialist.

Folded into the foundation work — no separate directory until the fork is chosen.

## Dev Commands

Atlas is one `uv` project. Work inside `atlas/`.

```bash
# One-time scaffold when starting Phase 0
uv init atlas
cd atlas
uv add --dev pytest ruff mypy

# Daily dev (from atlas/)
uv run python -m atlas            # run the CLI
uv run pytest                    # run all tests
uv run pytest tests/test_foo.py  # single test file
uv run pytest -k "test_name"     # single test by name
uv run ruff check .              # lint
uv run ruff format .             # format
uv run mypy src/                 # type check (goal: --strict clean)
```

## Conventions

- `uv` for package management (not pip/poetry)
- Ruff for lint/format, mypy for type checking (`mypy --strict` goal)
- 100% type hints on all new code
- Structured logging instead of `print()`
- pytest for tests; cover the main flow at minimum
- Pydantic v2 for data models

## Key Stack

Python-first, per phase:
- **00–01**: `openai` (or `anthropic`), `pytest`
- **02**: `fastapi`, `pydantic`, `httpx`, `uvicorn`
- **03**: `numpy`, `pgvector`, PostgreSQL, `langchain`, `llama-index`
- **04**: Langfuse (self-hosted), `ragas`
- **05**: Docker, AWS (`boto3`), S3/IAM/EC2

## Reference

- `ai-engineer-roadmap.md` — source of truth: full roadmap, real baselines, per-phase deliverables and anti-patterns. Read before scaffolding any new phase directory.
- `roadmaps/mercado-ai-engineer-2026.md` — condensed 2026 market intelligence for the target niche (demand, salaries/rates, in-demand stack, positioning).
- `_archive/` — earlier `agents/` work from a previous roadmap (MCP, LangGraph, capstone); kept for reference, not part of the current structure.
