"""Email triage agent — Pydantic AI implementation.

Same task as langgraph_agent.py. Focus on type-safety differences.
"""

from __future__ import annotations

from typing import Literal
from pydantic import BaseModel

# from pydantic_ai import Agent


class TriageResult(BaseModel):
    classification: Literal["urgent", "normal", "spam"]
    draft_reply: str | None
    escalated: bool
    reasoning: str


# TODO: define pydantic_ai.Agent with result_type=TriageResult
# TODO: add tools if needed
# TODO: run on same sample emails as langgraph_agent.py
