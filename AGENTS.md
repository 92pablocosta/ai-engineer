# Repository Guidelines

## Project Structure & Module Organization

This repository is an AI Engineer learning workspace organized around `ai-engineer-study-map.md`. Each top-level phase directory is intended to become an independent Python project:

- `python/`: advanced Python, FastAPI, async, Pydantic v2, PostgreSQL.
- `llm-api/`: OpenAI and Anthropic SDKs, prompt engineering.
- `rag/`: embeddings, vector stores, RAG pipelines, evaluation.
- `orchestration/`: LangChain LCEL, LangGraph, agents.
- `mpc/`: Model Context Protocol exercises.
- `eval-observability/`: LangSmith, LLM-as-judge, Ragas.
- `cloud/`: Docker, AWS, Modal, Railway, GitHub Actions.

Keep shared roadmap and agent guidance at the repository root. Put phase-specific source code, tests, and config in the relevant phase directory.

## Build, Test, and Development Commands

Use `uv` for Python projects. Run commands from the specific phase directory, not the repository root:

```bash
uv init .
uv add --dev pytest ruff mypy
uv run pytest
uv run ruff check .
uv run ruff format .
uv run mypy src/
```

`pytest` runs tests, `ruff check` lints, `ruff format` formats, and `mypy` type-checks. Add app-specific commands in that phase's README when it gains runnable services.

## Coding Style & Naming Conventions

Write Python with full type hints and aim for `mypy --strict` compatibility. Prefer Pydantic v2 models for schemas, configuration, and API I/O. Use structured logging instead of `print()`. Use `async`/`await` for I/O-bound API, database, or network work.

Use `snake_case` for modules, functions, variables, and test files; use `PascalCase` for classes and Pydantic models. Keep examples aligned with the current phase.

## Testing Guidelines

Use `pytest`. Place tests under `tests/` inside each phase project, with files named `test_*.py`. Cover each main flow plus edge cases for parsing, validation, API failures, and persistence where relevant.

Run before handing off Python changes:

```bash
uv run ruff check .
uv run mypy src/
uv run pytest
```

## Commit & Pull Request Guidelines

Current history uses short, imperative commit messages such as `add files` and `update gitignore`. Keep commits focused and concise, for example `add rag embedding exercise`.

Pull requests should describe the phase, learning objective, key changes, and validation commands run. Link relevant issues or roadmap sections. Include screenshots or logs only when UI, CLI output, or deployment behavior changed.

## Agent-Specific Instructions

Read `ai-engineer-study-map.md` before scaffolding or expanding a phase. Preserve the learning scope for the current phase, and avoid solving exercises with heavier abstractions than the roadmap intends.
