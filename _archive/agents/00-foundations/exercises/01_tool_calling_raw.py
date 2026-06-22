"""Exercise 01 — Tool calling via raw API (no agent framework).

Goal: understand the tool call roundtrip at the protocol level.
  1. Define a tool JSON schema manually.
  2. Send a user message that should trigger the tool.
  3. Parse the tool_use block from the response.
  4. Execute the tool locally.
  5. Send the tool result back and get the final answer.

Run: uv run python exercises/01_tool_calling_raw.py
"""

from __future__ import annotations

import json
import os


# TODO: define a simple tool — e.g. get_weather(city: str) -> str
# Return a mocked/hardcoded result for now; focus is on the protocol.
TOOLS: list[dict] = [
    # TODO: fill in JSON schema for your tool
]


def call_tool(name: str, args: dict) -> str:
    """Execute tool locally and return string result."""
    # TODO: implement dispatch
    raise NotImplementedError


def run() -> None:
    """Full tool-calling roundtrip."""
    # TODO:
    # 1. Initialize Anthropic (or OpenAI) client
    # 2. Send initial message with TOOLS
    # 3. Check if response contains a tool_use block
    # 4. If yes: extract name + input, call call_tool(), send result back
    # 5. Print final text response
    raise NotImplementedError


if __name__ == "__main__":
    run()
