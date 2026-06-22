"""Exercise 02 — MCP client: list and call tools.

Goal: understand the client side of the MCP protocol.
  1. Connect to the server from ex01 via stdio transport.
  2. List all available tools and resources.
  3. Call each tool and print the result.
  4. Read the resource.

Run (server must be runnable as subprocess):
  uv run python exercises/02_mcp_client.py
"""

from __future__ import annotations

import asyncio

# from mcp import ClientSession, StdioServerParameters
# from mcp.client.stdio import stdio_client


async def main() -> None:
    # TODO:
    # server_params = StdioServerParameters(
    #     command="uv", args=["run", "python", "exercises/01_mcp_server.py"]
    # )
    # async with stdio_client(server_params) as (read, write):
    #     async with ClientSession(read, write) as session:
    #         await session.initialize()
    #         tools = await session.list_tools()
    #         print("Tools:", [t.name for t in tools.tools])
    #         resources = await session.list_resources()
    #         print("Resources:", [r.uri for r in resources.resources])
    #         # call a tool
    #         result = await session.call_tool("calculate", {"expression": "2**10"})
    #         print("Result:", result)
    raise NotImplementedError


if __name__ == "__main__":
    asyncio.run(main())
