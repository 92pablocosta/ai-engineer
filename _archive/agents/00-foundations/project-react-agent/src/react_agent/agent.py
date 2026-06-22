"""AgentRunner — main ReAct loop.

No framework. Just SDK + Python.
"""

from __future__ import annotations

import logging
import os
import sys

from react_agent.loop import ExecutionTrace, ReActStep, StepType
from react_agent.tools import dispatch, get_tool_schemas

logger = logging.getLogger(__name__)

MAX_ITER = int(os.getenv("MAX_ITER", "10"))


class AgentRunner:
    """Runs the ReAct loop for a given question."""

    def __init__(self, max_iter: int = MAX_ITER) -> None:
        self.max_iter = max_iter
        # TODO: initialize OpenAI client — openai.OpenAI()

    def run(self, question: str) -> ExecutionTrace:
        """Execute ReAct loop and return full trace."""
        trace = ExecutionTrace(question=question)
        messages: list[dict] = [{"role": "user", "content": question}]

        for step_num in range(self.max_iter):
            # TODO:
            # 1. Call LLM with current messages + tool schemas
            # 2. If response is final text answer → log FINAL step, return trace
            # 3. If response has tool_use → log REASON + ACTION steps
            # 4. Execute tool via dispatch(), log OBSERVATION
            # 5. Append tool result to messages, continue loop
            raise NotImplementedError

        logger.warning("Hit MAX_ITER=%d without final answer", self.max_iter)
        # TODO: add a FINAL step noting max iterations reached, return trace
        return trace


def main() -> None:
    logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
    if len(sys.argv) < 2:
        print("Usage: python -m react_agent '<question>'")
        sys.exit(1)

    question = " ".join(sys.argv[1:])
    runner = AgentRunner()
    trace = runner.run(question)
    print(trace.summary())


if __name__ == "__main__":
    main()
