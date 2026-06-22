"""Tests for LLM judge logic."""

from __future__ import annotations

import pytest

from eval_pipeline.judge import JudgeScore


class TestJudgeScore:
    def test_overall_is_mean_of_axes(self) -> None:
        score = JudgeScore(correctness=3, guardrail_compliance=2, helpfulness=1, reasoning="test")
        assert score.overall == pytest.approx(2.0)

    def test_perfect_score(self) -> None:
        score = JudgeScore(correctness=3, guardrail_compliance=3, helpfulness=3, reasoning="test")
        assert score.overall == 3.0

    def test_minimum_score(self) -> None:
        score = JudgeScore(correctness=1, guardrail_compliance=1, helpfulness=1, reasoning="test")
        assert score.overall == 1.0

    def test_invalid_score_rejected(self) -> None:
        from pydantic import ValidationError
        with pytest.raises(ValidationError):
            JudgeScore(correctness=4, guardrail_compliance=1, helpfulness=1, reasoning="test")
