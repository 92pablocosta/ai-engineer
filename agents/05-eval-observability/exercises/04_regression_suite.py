"""Exercise 04 — Regression suite that fails on quality drop.

Goal: detect quality regressions automatically before they reach users.
  1. Load golden dataset from ex02.
  2. Run each case through the agent.
  3. Score each response with LLM judge from ex03.
  4. Compute success_rate = % of cases with overall >= threshold.
  5. Exit with code 1 if success_rate < MIN_SUCCESS_RATE.

This should run in CI on every prompt change.

Run: uv run python exercises/04_regression_suite.py
Exit code 0 = passed. Exit code 1 = regression detected.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

MIN_SUCCESS_RATE = 0.80  # 80% pass rate required
SCORE_THRESHOLD = 2.0    # case passes if overall >= this


@dataclass
class EvalResult:
    case_id: str
    question: str
    response: str
    score: float
    passed: bool
    reasoning: str


def run_suite(golden_path: str = "golden_dataset.json") -> list[EvalResult]:
    """Run all golden cases, return scored results."""
    # TODO:
    # 1. Load golden dataset
    # 2. For each case: run agent, judge response
    # 3. passed = score.overall >= SCORE_THRESHOLD
    raise NotImplementedError


def report(results: list[EvalResult]) -> None:
    """Print results table and pass/fail summary."""
    # TODO: print table with: case_id | passed | score | reasoning[:50]
    # print: "X/Y passed (Z%). PASSED" or "X/Y passed (Z%). REGRESSION DETECTED"
    raise NotImplementedError


if __name__ == "__main__":
    results = run_suite()
    report(results)
    success_rate = sum(r.passed for r in results) / len(results)
    sys.exit(0 if success_rate >= MIN_SUCCESS_RATE else 1)
