"""Exercise 03 — Human-in-the-loop with interrupt_before.

Goal: pause the graph at a risky node, wait for human approval, then resume.
  1. Add an "approval" node before any destructive tool execution.
  2. Use interrupt_before=["approval"] so graph pauses there.
  3. Inspect pending state.
  4. Resume with graph.invoke(None, config) after human says yes/no.

Run: uv run python exercises/03_human_in_loop.py
"""

from __future__ import annotations

# from langgraph.graph import StateGraph, END
# from langgraph.checkpoint.sqlite import SqliteSaver


def approval_node(state: dict) -> dict:
    """Human approval gate. Should never be called directly — graph pauses before it."""
    # TODO: if human approved (check state["approved"]):
    #   proceed to tool execution
    # else:
    #   add cancellation message, go to END
    raise NotImplementedError


def build_graph_with_hitl(checkpointer):
    """Graph with human-in-the-loop before destructive actions."""
    # TODO: same as ex01 but add approval_node between llm and tools
    # compile with interrupt_before=["approval"]
    raise NotImplementedError


if __name__ == "__main__":
    # TODO:
    # 1. Build graph, send message that triggers a destructive tool
    # 2. Graph pauses — print pending tool call for human review
    # 3. Prompt human: "Approve? (y/n)"
    # 4. If y: graph.update_state(config, {"approved": True}); graph.invoke(None, config)
    # 5. If n: graph.update_state(config, {"approved": False}); graph.invoke(None, config)
    pass
