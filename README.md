# AI Engineer — learning in public

Public record of my path toward production AI/Backend Engineering. This repository is a learning **log**: every exercise, test, and decision is meant to prove real understanding — not to build a portfolio of polished projects.

**The differentiator is the commit history, not a finished app.** Commits track learning milestones with clear messages, so the `git log` itself shows the progression: Python fundamentals → tests → API → RAG → evals → deployment.

## Structure

```text
.
├── learning/    # Python, pytest, and FastAPI exercises
├── 03-rag/      # retrieval-augmented generation, built from numpy up
├── 04-evals-observability/  # evals and observability (phase 4, not started)
├── 05-docker-aws/           # Docker and AWS deployment (phase 5, not started)
├── docs/        # roadmap and public documentation of the journey
└── roadmaps/    # broader market/career roadmap notes
```

Exercises are organized by subject, not as versions of one product. An original project will only be chosen once the necessary foundations are solid. Credentials, virtual environments, caches, and local data are excluded from Git via [`.gitignore`](.gitignore).

## Foundation progress

| Phase | Focus |
| --- | --- |
| 0 | Python, OOP, type hints, and async |
| 1 | pytest, fixtures, and mocks |
| 2 | FastAPI, Pydantic, and streaming |
| 3 | Embeddings, retrieval, pgvector, and RAG |
| 4 | Evals, tracing, and observability |
| 5 | Docker, AWS, and S3 |

Read the [full roadmap](docs/roadmap.md) before starting a phase. During foundation exercises, code is hand-written; AI steps in afterward only to review and unblock — not to write it.

## Development

Each exercise documents its own commands and dependencies. For the current pytest track:

```bash
cd learning/pytest
python3 -m pytest -q project1
```

Future standalone projects use `uv`, Ruff, mypy, and pytest from the start.
