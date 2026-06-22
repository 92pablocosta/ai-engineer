"""Exercise 03 — Retry with exponential backoff.

Goal: make LLM calls resilient to transient failures.
  1. Implement retry decorator / wrapper with exponential backoff.
  2. Simulate failures (mock a flaky API call).
  3. Add jitter so parallel retries don't thunderherd.
  4. Log each attempt with wait time.
  5. Raise after max_retries exhausted.

Run: uv run python exercises/03_retry_backoff.py
"""

from __future__ import annotations

import logging
import random
import time
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

logger = logging.getLogger(__name__)
F = TypeVar("F", bound=Callable[..., Any])


def retry_with_backoff(
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[F], F]:
    """Decorator: retry on specified exceptions with exponential backoff + jitter."""
    # TODO: implement
    # delay formula: min(base_delay * 2**attempt + random.uniform(0, 1), max_delay)
    # log each retry: attempt number, exception, wait time
    # raise last exception after max_retries
    raise NotImplementedError


# TODO: define a flaky_llm_call() that fails the first N times, then succeeds.
# Use it to demo the decorator works.

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # TODO: call flaky_llm_call() wrapped with retry_with_backoff and print result
