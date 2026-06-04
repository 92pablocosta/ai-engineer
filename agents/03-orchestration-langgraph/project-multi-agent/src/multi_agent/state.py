"""AgentState definition and reducers."""

from __future__ import annotations

import operator
from typing import Annotated, Literal, TypedDict


class AgentState(TypedDict):
    task: str
    messages: Annotated[list, operator.add]
    research_notes: str | None
    draft: str | None
    review_feedback: str | None
    approved: bool
    next_worker: Literal["researcher", "writer", "reviewer", "human", "__end__"] | None
