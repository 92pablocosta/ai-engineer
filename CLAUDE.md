# CLAUDE.md

## Purpose

AI Engineer learning workspace. This is a learning **log**, not a product portfolio. The current goal is to build defensible foundations phase by phase, following `docs/roadmap.md`; no capstone or spine project has been chosen yet.

**The differentiator is the commit history, not a polished final app.** Commit meaningful learning milestones with clear messages: Python fundamentals → tests → API → RAG → evals → deployment.

## The learning rule (overrides convenience)

**During the foundation phases, AI writes no code for the user.** The user writes exercises by hand, hits errors, reads tracebacks, then checks against AI. When asked to "build" or "do" a foundation exercise, prefer to *guide, review, and unblock* — do not hand over finished solutions unless the user explicitly asks for the answer.

## Structure

```text
ai-engineer/
├── README.md
├── docs/roadmap.md      ← source of truth for the learning plan
├── learning/            ← small, hand-written exercises by subject
└── archive/             ← previous experiments, outside the current plan
```

Keep exercises small and focused. Do not scaffold empty phase folders or choose a new product on the user's behalf. When the user chooses an original project, create it deliberately with a `src/` layout, tests and a README.

## Current phase path

The roadmap is sequential:

| Phase | Focus | Evidence of learning |
| --- | --- | --- |
| 0 | Python, OOP, type hints and async | small hand-written programs and clear reasoning |
| 1 | pytest, fixtures, parametrization and mocks | green tests over code the user understands |
| 2 | FastAPI, Pydantic, DI and streaming | a small tested API |
| 3 | numpy retrieval → pgvector → framework | explain each layer without the framework |
| 4 | evals and observability | versioned measurements and a documented improvement |
| 5 | Docker and AWS | a reproducible deployment of a future original project |

Phase 3 ordering is mandatory: by hand (numpy) → pgvector → only then LangChain → LlamaIndex tour. Do not start from the framework.

## Commands

Follow the instructions local to each exercise. For the current pytest material:

```bash
cd learning/pytest
python3 -m pytest -q project1
```

When a future standalone project begins, use `uv`, Ruff, mypy and pytest. Do not add a package configuration before there is real code to support it.

## Conventions

- `uv` for new standalone Python projects (not pip/poetry)
- Ruff for lint/format, mypy for type checking (`mypy --strict` goal)
- 100% type hints on new production-oriented code
- Structured logging instead of `print()` outside learning exercises
- pytest for tests; cover the main flow at minimum
- Pydantic v2 for API models

## Reference

- `docs/roadmap.md` — source of truth for scope, sequence and deliverables.
- `learning/` — current hand-written exercises and their local guidance.
- `archive/` — previous experiments kept for reference, not part of the current plan.
