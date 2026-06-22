"""Support AgentRunner with persistent memory and guardrails."""

from __future__ import annotations

from support_agent.guardrails import check_output
from support_agent.memory import SessionMemory, Turn
from support_agent.tools import get_tool_schemas


class SupportAgent:
    def __init__(self, memory: SessionMemory, max_iter: int = 10) -> None:
        self.memory = memory
        self.max_iter = max_iter
        # TODO: init LLM client

    async def chat(self, session_id: str, user_message: str) -> str:
        """Process one user turn, return agent reply."""
        # TODO:
        # 1. Load session history from memory
        # 2. Append user turn
        # 3. Run ReAct loop (max_iter) with tools
        # 4. On tool call: check guardrails, execute, observe
        # 5. Apply output guardrail before returning
        # 6. Persist assistant turn
        # 7. Return reply text
        raise NotImplementedError
