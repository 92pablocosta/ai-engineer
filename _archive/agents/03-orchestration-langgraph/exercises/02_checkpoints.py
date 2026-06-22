"""Exercise 02 — Checkpoints and durable execution.

Goal: understand how LangGraph survives process restarts.
  1. Add SqliteSaver (or PostgresSaver) as checkpointer to the graph.
  2. Start a conversation, interrupt mid-run (KeyboardInterrupt or manual stop).
  3. Resume from the last checkpoint with the same thread_id.
  4. Verify the conversation context was preserved.

Run: uv run python exercises/02_checkpoints.py
"""

from __future__ import annotations

# from langgraph.checkpoint.sqlite import SqliteSaver

CHECKPOINT_DB = "checkpoints.db"
THREAD_ID = "demo-thread-001"


def build_graph_with_checkpoints(checkpointer):
    """Same graph as ex01 but with checkpointer attached."""
    # TODO: reuse build_graph() from ex01, pass checkpointer to .compile()
    raise NotImplementedError


if __name__ == "__main__":
    # TODO:
    # with SqliteSaver.from_conn_string(CHECKPOINT_DB) as checkpointer:
    #     graph = build_graph_with_checkpoints(checkpointer)
    #     config = {"configurable": {"thread_id": THREAD_ID}}
    #
    #     # First run
    #     graph.invoke({"messages": [{"role": "user", "content": "Olá"}]}, config)
    #
    #     # Simulate restart — reload checkpointer, same thread_id
    #     result = graph.invoke({"messages": [{"role": "user", "content": "Qual foi minha última pergunta?"}]}, config)
    #     print(result["messages"][-1].content)
    pass
