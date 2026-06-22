"""Langfuse tracing helpers."""

from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Any, Generator


def is_enabled() -> bool:
    return os.getenv("LANGFUSE_ENABLED", "false").lower() == "true"


@contextmanager
def trace_agent_call(
    name: str,
    input: dict[str, Any],
    session_id: str | None = None,
    user_id: str | None = None,
) -> Generator[Any, None, None]:
    """Context manager that creates a Langfuse trace if tracing is enabled."""
    # TODO:
    # if not is_enabled(): yield None; return
    # trace = langfuse.trace(name=name, input=input, session_id=session_id, user_id=user_id)
    # try: yield trace
    # finally: trace.update(output=...) if output captured
    raise NotImplementedError


def log_llm_span(trace: Any, model: str, input_tokens: int, output_tokens: int, cost: float) -> None:
    """Attach LLM usage span to a trace."""
    # TODO: trace.generation(model=model, usage=..., ...)
    raise NotImplementedError
