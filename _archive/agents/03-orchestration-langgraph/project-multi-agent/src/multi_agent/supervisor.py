"""Supervisor node — routes tasks to worker agents."""

from __future__ import annotations

from multi_agent.state import AgentState


def supervisor_node(state: AgentState) -> dict:
    """Decide which worker to call next based on current state."""
    # TODO: call LLM with task + current state
    # LLM returns next_worker: "researcher" | "writer" | "reviewer" | "human" | "__end__"
    raise NotImplementedError


def route(state: AgentState) -> str:
    """Conditional edge function: return worker name from state."""
    return state.get("next_worker") or "__end__"
