"""Regression suite runner."""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from eval_pipeline.judge import JudgeScore, judge

MIN_SUCCESS_RATE = float(os.getenv("MIN_SUCCESS_RATE", "0.80"))
SCORE_THRESHOLD = float(os.getenv("SCORE_THRESHOLD", "2.0"))
GOLDEN_DATASET_PATH = Path(__file__).parent.parent.parent / "data" / "golden_dataset.json"


@dataclass
class EvalResult:
    case_id: str
    question: str
    response: str
    score: JudgeScore
    passed: bool


def load_golden_dataset() -> list[dict]:
    return json.loads(GOLDEN_DATASET_PATH.read_text())


def run_agent(question: str) -> str:
    """Call the agent under evaluation. Replace with your agent's entrypoint."""
    # TODO: import and call your agent here
    raise NotImplementedError


def run() -> list[EvalResult]:
    """Run all golden cases, return results."""
    cases = load_golden_dataset()
    results = []
    for case in cases:
        response = run_agent(case["input"])
        score = judge(case["input"], response)
        results.append(EvalResult(
            case_id=case["id"],
            question=case["input"],
            response=response,
            score=score,
            passed=score.overall >= SCORE_THRESHOLD,
        ))
    return results


def print_report(results: list[EvalResult]) -> None:
    n_passed = sum(r.passed for r in results)
    rate = n_passed / len(results) if results else 0
    print(f"\n{'Case ID':<20} {'Pass':<6} {'Score':<6} {'Reasoning'}")
    print("-" * 80)
    for r in results:
        print(f"{r.case_id:<20} {'OK' if r.passed else 'FAIL':<6} {r.score.overall:.1f}   {r.score.reasoning[:50]}")
    print("-" * 80)
    status = "PASSED" if rate >= MIN_SUCCESS_RATE else "REGRESSION DETECTED"
    print(f"{n_passed}/{len(results)} passed ({rate:.0%}). {status}")


if __name__ == "__main__":
    results = run()
    print_report(results)
    rate = sum(r.passed for r in results) / len(results)
    sys.exit(0 if rate >= MIN_SUCCESS_RATE else 1)
