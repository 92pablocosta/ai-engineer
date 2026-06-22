"""Exercise 01 — Instrument an agent with Langfuse tracing.

Goal: every LLM call and tool call becomes a searchable span.
  1. Set up Langfuse client (self-hosted or cloud).
  2. Wrap an existing agent's LLM calls with langfuse.trace / span.
  3. Run 5 queries, verify traces appear in Langfuse UI.
  4. Add metadata: session_id, user_id, model, input_tokens, cost.

Langfuse self-host: docker compose up on your VPS.
Docs: https://langfuse.com/docs/get-started

Run: uv run python exercises/01_langfuse_tracing.py
"""

from __future__ import annotations

import os

# from langfuse import Langfuse
# from langfuse.decorators import observe, langfuse_context


# TODO: init langfuse client
# langfuse = Langfuse(
#     public_key=os.environ["LANGFUSE_PUBLIC_KEY"],
#     secret_key=os.environ["LANGFUSE_SECRET_KEY"],
#     host=os.environ["LANGFUSE_HOST"],
# )


# TODO: decorate your agent's main function with @observe()
# @observe()
# def run_agent(question: str) -> str:
#     langfuse_context.update_current_trace(name="support-agent", user_id="test-user")
#     # ... existing agent logic ...
#     pass


if __name__ == "__main__":
    questions = [
        "Qual o horário de atendimento?",
        "Como cancelo minha consulta?",
        "Quais convênios vocês aceitam?",
    ]
    for q in questions:
        print(f"Q: {q}")
        # result = run_agent(q)
        # print(f"A: {result}\n")
    # langfuse.flush()
