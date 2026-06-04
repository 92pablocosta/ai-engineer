# GEMINI.md - AI Engineer Workspace

This file provides instructional context for Gemini CLI when working in this repository.

## Project Overview
This is a structured learning workspace for **Pablo Costa** to transition into an **AI Engineer** role. The project is organized around a 14-week study map (`ai-engineer-study-map.md`) covering advanced Python, LLM APIs, RAG, Orchestration, and Cloud deployment.

Each directory represents a specific phase of the curriculum. While currently containing empty stubs, these directories will evolve into independent Python projects.

## Directory Structure & Phases

| Directory | Phase | Focus |
| :--- | :--- | :--- |
| `python/` | 1 (Weeks 1-3) | Advanced Python, FastAPI, Pydantic v2, PostgreSQL |
| `llm-api/` | 2 (Weeks 4-5) | OpenAI & Anthropic SDKs, Prompt Engineering |
| `rag/` | 3 (Weeks 6-8) | Embeddings, pgvector, RAG pipelines, Evals |
| `orchestration/` | 4 (Weeks 9-10) | LangChain LCEL, LangGraph, Agents |
| `mpc/` | 5 (Week 11) | Model Context Protocol (MCP) |
| `eval-observability/` | 6 (Week 12) | LangSmith, LLM-as-judge, Ragas |
| `cloud/` | 7 (Weeks 13-14) | Docker, AWS, Modal, GitHub Actions |

## Key Documents
- `ai-engineer-study-map.md`: The master roadmap containing resources, domain checks, and anti-patterns. **Consult this before starting any new phase.**
- `CLAUDE.md`: Guidelines for Claude Code (mirrored here for consistency).
- `README.md`: Project landing page (currently minimal).

## Development Standards
When adding code to any phase directory, strictly adhere to the following:

- **Package Management:** Use `uv` exclusively. Each phase is an independent `uv` project.
- **Type Safety:** 100% type hints are mandatory. Use `mypy --strict` as the goal.
- **Linting & Formatting:** Use `ruff`.
- **Testing:** Use `pytest`. Every main flow must have test coverage.
- **Data Modeling:** Use `Pydantic v2` for all I/O, schemas, and configurations.
- **Logging:** Use structured logging (e.g., `structlog`) instead of `print()`.
- **Async:** Use `async/await` for all I/O-bound operations (API calls, DB, etc.).

## Common Commands
Execute these within the specific phase directory:

```bash
# Initialize a new phase
uv init .
uv add --dev pytest ruff mypy

# Development Loop
uv run ruff check .        # Linting
uv run ruff format .       # Formatting
uv run mypy src/           # Type checking
uv run pytest              # Testing
```

## Guidance for Gemini
- **Educational Context:** Recognize that this is a learning repository. When asked to help with a task, refer to the corresponding phase in `ai-engineer-study-map.md` to ensure the solution aligns with the intended learning depth (e.g., "SDK-only" vs "Framework").
- **Proactive Validation:** Always suggest or run `ruff`, `mypy`, and `pytest` when modifications are made to Python code.
- **Surgical Updates:** When helping Pablo with exercises, focus on the specific domain check or task at hand without over-engineering beyond the current phase's scope.
