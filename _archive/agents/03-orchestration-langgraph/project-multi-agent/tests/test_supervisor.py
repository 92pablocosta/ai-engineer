"""Tests for supervisor routing logic."""

from __future__ import annotations

import pytest

from multi_agent.state import AgentState
from multi_agent.supervisor import route


class TestRoute:
    def test_routes_to_researcher_when_no_notes(self) -> None:
        # TODO: state with no research_notes → route should return "researcher"
        pytest.skip("not implemented")

    def test_routes_to_end_when_approved(self) -> None:
        # TODO: state with approved=True → route returns "__end__"
        pytest.skip("not implemented")

    def test_routes_to_writer_after_research(self) -> None:
        # TODO: state with research_notes set, no draft → "writer"
        pytest.skip("not implemented")
