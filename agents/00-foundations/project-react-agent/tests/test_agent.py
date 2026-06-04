"""Tests for ReAct agent."""

from __future__ import annotations

import pytest

from react_agent.loop import ExecutionTrace, ReActStep, StepType
from react_agent.tools import calculator, dispatch, web_search


class TestCalculator:
    def test_basic_arithmetic(self) -> None:
        # TODO: assert calculator("2 + 2") == 4.0
        pytest.skip("not implemented")

    def test_sqrt(self) -> None:
        # TODO: assert calculator("sqrt(144)") == 12.0
        pytest.skip("not implemented")

    def test_rejects_arbitrary_code(self) -> None:
        # TODO: assert raises ValueError/PermissionError for "import os; os.system(...)"
        pytest.skip("not implemented")


class TestDispatch:
    def test_unknown_tool_returns_error_string(self) -> None:
        # TODO: result = dispatch("nonexistent_tool", {})
        # assert "ToolError" in result or "unknown" in result.lower()
        pytest.skip("not implemented")

    def test_calculator_via_dispatch(self) -> None:
        # TODO: result = dispatch("calculator", {"expression": "3 * 4"})
        # assert "12" in result
        pytest.skip("not implemented")


class TestExecutionTrace:
    def test_summary_includes_step_count(self) -> None:
        # TODO: build a trace with 3 steps, assert summary contains "3"
        pytest.skip("not implemented")

    def test_max_iter_enforced(self) -> None:
        # TODO: mock LLM to never return final answer,
        # assert runner.run() returns trace with max_iter steps
        pytest.skip("not implemented")
