"""LangGraph agent that uses MCP tools dynamically."""

from __future__ import annotations

from mcp_agent.client import MCPClient


class MCPAgent:
    def __init__(self, mcp_client: MCPClient) -> None:
        self.client = mcp_client
        # TODO: build LangGraph agent that uses mcp_client.call_tool as tool executor

    async def run(self, question: str) -> str:
        """Answer question using MCP tools discovered at runtime."""
        # TODO:
        # 1. list_tools() from MCP server
        # 2. Convert to LangGraph-compatible tool list
        # 3. Run agent graph with those tools
        # 4. Return final answer
        raise NotImplementedError
