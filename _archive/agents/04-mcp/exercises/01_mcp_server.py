"""Exercise 01 — MCP server with FastMCP.

Goal: build a minimal MCP server exposing tools and a resource.
  1. Create a FastMCP server.
  2. Add 2 tools: one that computes something, one that calls an API.
  3. Add 1 resource: read-only data endpoint (e.g. current config or a dataset).
  4. Run server in stdio mode and test via ex02.

Run: uv run python exercises/01_mcp_server.py
"""

from __future__ import annotations

# from mcp.server.fastmcp import FastMCP

# app = FastMCP("demo-server")


# TODO: implement
# @app.tool()
# def calculate(expression: str) -> float:
#     """Evaluate a math expression."""
#     ...

# @app.tool()
# def get_current_time(timezone: str = "America/Recife") -> str:
#     """Return current time in given timezone."""
#     ...

# @app.resource("config://settings")
# def get_settings() -> str:
#     """Return server configuration as JSON string."""
#     ...


if __name__ == "__main__":
    # app.run(transport="stdio")
    pass
