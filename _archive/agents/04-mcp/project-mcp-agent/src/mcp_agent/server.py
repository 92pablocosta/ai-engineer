"""FastMCP server — HTTP/SSE transport."""

from __future__ import annotations

import os

# from mcp.server.fastmcp import FastMCP

# app = FastMCP("rag-mcp-server")

# TODO: implement tools and resources
# @app.tool()
# def search_knowledge(query: str, top_k: int = 5) -> str: ...

# @app.tool()
# def create_document(title: str, content: str) -> dict: ...

# @app.resource("rag://corpus/stats")
# def corpus_stats() -> str: ...

# @app.prompt("answer_template")
# def answer_template(question: str) -> str: ...


if __name__ == "__main__":
    port = int(os.getenv("MCP_SERVER_PORT", "8001"))
    # app.run(transport="sse", port=port)
    pass
