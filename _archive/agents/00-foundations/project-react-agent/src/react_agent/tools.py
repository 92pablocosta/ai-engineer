"""Tool implementations and registry.

Each tool: callable Python function + JSON schema for the LLM.
Registry maps tool name → (function, schema).
"""

from __future__ import annotations

import math
from typing import Any


# --- Tool implementations ---

def calculator(expression: str) -> float:
    """Evaluate a safe mathematical expression."""
    # TODO: implement safely (no eval on arbitrary input — use ast.literal_eval
    # or a math parser). Allowed: basic arithmetic, sqrt, pow, etc.
    raise NotImplementedError


def web_search(query: str) -> str:
    """Mock web search — returns hardcoded snippets for known queries."""
    # TODO: implement mock with a small dict of query → result
    # For unknown queries return "No results found for: {query}"
    raise NotImplementedError


def read_file(path: str) -> str:
    """Read a file from data/ directory (sandboxed)."""
    # TODO: validate path stays inside data/, raise PermissionError otherwise
    raise NotImplementedError


# --- Registry ---

TOOL_REGISTRY: dict[str, Any] = {
    # "tool_name": {"fn": callable, "schema": {...}}
    # TODO: populate after implementing tools above
}


def get_tool_schemas() -> list[dict[str, Any]]:
    """Return list of tool schemas for the LLM API call."""
    # TODO: extract schemas from TOOL_REGISTRY
    raise NotImplementedError


def dispatch(name: str, args: dict[str, Any]) -> str:
    """Call tool by name, return string result or error message."""
    # TODO: look up in registry, call fn(**args), return str(result)
    # Catch all exceptions and return "ToolError: {e}" — don't crash the loop
    raise NotImplementedError
