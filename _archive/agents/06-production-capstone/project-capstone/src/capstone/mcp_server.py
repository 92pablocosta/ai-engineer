"""MCP server for the capstone system."""

from __future__ import annotations

import os

# from mcp.server.fastmcp import FastMCP

# app = FastMCP("capstone-server")

# TODO: expose RAG search as tool
# TODO: expose domain-specific tools (appointments, documents, etc.)
# TODO: expose corpus stats as resource

if __name__ == "__main__":
    port = int(os.getenv("MCP_SERVER_PORT", "8001"))
    # app.run(transport="sse", port=port)
    pass
