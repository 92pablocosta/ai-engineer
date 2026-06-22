# AGENTS.md

## Purpose

- This folder is for learning pytest from zero with a teaching workflow, not for generating finished solutions.
- The user writes exercise code by hand; agents should explain, review, interpret tracebacks, and unblock.
- Do not rewrite user exercise code just to make tests pass unless the user explicitly asks for direct code changes.

## Learning Plan

- Continue from `PROGRESS.md`; it records completed lessons and the next lesson.
- Current path: `01-pytest/`.
- Current exercise code lives in `project1/`.
- Focus sequence: `assert` and failure reading, `pytest.raises`, `@pytest.mark.parametrize`, fixtures, `tmp_path`, monkeypatch/mocking, async tests with `pytest-asyncio`, then a small AI assistant test project without real API calls.

## Commands

- From `01-pytest/project1/`: `python -m pytest -q`.
- From `01-pytest/`: `python -m pytest -q project1`.
- If pytest is missing in `project1/`, use a local venv there: `python -m venv .venv`, `source .venv/bin/activate`, `python -m pip install -U pytest`.
- `project1/` has no `pyproject.toml`; do not assume `uv run` works here.

## Teaching Style

- Keep lessons small: concept, exercise, user runs pytest, then review output.
- Prefer making the user read pytest failure output instead of hiding it.
- For AI Engineer relevance, emphasize tests that avoid real network calls, OpenAI/Anthropic calls, databases, or hidden external state.
- Always update `PROGRESS.md` at the end of a lesson or when the user pauses, so the next session can continue from the exact stopping point.
- `PROGRESS.md` should record: lesson status, files touched by the user, concepts learned, commands run, important pytest output or traceback interpretation, and the next lesson.
