"""Exercise 03 — Expose RAG pipeline as MCP resource + tool.

Goal: the RAG system from Stage 02 becomes a MCP-accessible service.
  1. resource("rag://corpus/list") → list available docs
  2. tool search_knowledge(query, top_k) → returns chunks with citations
  3. An agent that doesn't know the RAG implementation can use it via MCP.

Run: uv run python exercises/03_rag_as_resource.py
"""

from __future__ import annotations

# from mcp.server.fastmcp import FastMCP
# Assumes Stage 02 agentic_rag package is importable

# app = FastMCP("rag-server")


# TODO:
# @app.resource("rag://corpus/list")
# def list_corpus() -> str:
#     """Return JSON list of indexed documents."""
#     ...

# @app.tool()
# def search_knowledge(query: str, top_k: int = 5) -> str:
#     """Search the knowledge base. Returns top_k chunks with doc_id citations."""
#     ...


if __name__ == "__main__":
    # app.run(transport="stdio")
    pass
