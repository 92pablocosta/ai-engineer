"""Email triage agent — LangGraph implementation.

Task: classify email (urgent/normal/spam), draft reply, escalate if urgent.
"""

from __future__ import annotations

from typing import Annotated, Literal, TypedDict
import operator


class TriageState(TypedDict):
    email: str
    classification: Literal["urgent", "normal", "spam"] | None
    draft_reply: str | None
    escalated: bool
    messages: Annotated[list, operator.add]


# TODO: implement nodes:
# - classify_node(state) -> {classification: ...}
# - draft_reply_node(state) -> {draft_reply: ...}
# - escalate_node(state) -> {escalated: True}

# TODO: build and compile graph
# Entry: classify → conditional:
#   urgent → draft_reply → escalate → END
#   normal → draft_reply → END
#   spam → END
