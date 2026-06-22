"""MCP client wrapper — discovers tools dynamically from server."""

from __future__ import annotations

import os
from typing import Any


class MCPClient:
    """Thin async wrapper around MCP ClientSession for use in agents."""

    def __init__(self, server_url: str) -> None:
        self.server_url = server_url
        # TODO: store SSE client session

    async def connect(self) -> None:
        """Initialize MCP session and list available tools."""
        # TODO: connect via sse_client, initialize session, list_tools
        raise NotImplementedError

    async def list_tools(self) -> list[dict]:
        """Return tool definitions in LangChain/LangGraph tool format."""
        # TODO: session.list_tools() → convert to {name, description, input_schema}
        raise NotImplementedError

    async def call_tool(self, name: str, arguments: dict[str, Any]) -> str:
        """Call a tool on the MCP server, return result as string."""
        # TODO: session.call_tool(name, arguments)
        raise NotImplementedError

    async def read_resource(self, uri: str) -> str:
        """Read a resource from the MCP server."""
        # TODO: session.read_resource(uri)
        raise NotImplementedError

    async def close(self) -> None:
        """Close session."""
        raise NotImplementedError
