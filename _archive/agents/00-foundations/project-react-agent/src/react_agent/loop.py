"""ReAct loop data structures and step logger."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

logger = logging.getLogger(__name__)


class StepType(str, Enum):
    REASON = "reason"
    ACTION = "action"
    OBSERVATION = "observation"
    FINAL = "final"


@dataclass
class ReActStep:
    step: int
    type: StepType
    content: str
    tool_name: str | None = None
    tool_args: dict[str, Any] | None = None
    tokens_used: int = 0


@dataclass
class ExecutionTrace:
    question: str
    steps: list[ReActStep] = field(default_factory=list)
    total_input_tokens: int = 0
    total_output_tokens: int = 0

    # TODO: add property cost_usd that calculates from token counts + model pricing
    # TODO: add method log_step(step: ReActStep) that appends and logs to logger

    def summary(self) -> str:
        """Return human-readable execution summary."""
        # TODO: implement
        raise NotImplementedError
