"""Worker agent nodes: Researcher, Writer, Reviewer."""

from __future__ import annotations

from multi_agent.state import AgentState


def researcher_node(state: AgentState) -> dict:
    """Research task, return notes. Updates research_notes."""
    # TODO: call LLM (+ optional RAG tool) to gather information
    raise NotImplementedError


def writer_node(state: AgentState) -> dict:
    """Write draft based on research_notes. Updates draft."""
    # TODO: call LLM with task + research_notes → produce draft
    raise NotImplementedError


def reviewer_node(state: AgentState) -> dict:
    """Review draft. Either approves or returns feedback for rewrite."""
    # TODO: call LLM with task + draft → {approved: bool, feedback: str}
    # Update approved and review_feedback
    raise NotImplementedError
