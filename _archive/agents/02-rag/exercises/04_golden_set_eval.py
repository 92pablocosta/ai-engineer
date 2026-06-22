"""Exercise 04 — Build golden dataset and compute recall@k + MRR.

Goal: move from "I think retrieval works" to "retrieval works at X%".
  1. Create 20 question → [relevant_doc_ids] pairs. Be strict about relevance.
  2. Run your retrieval system on all 20 queries.
  3. Compute recall@1, recall@5, MRR.
  4. Write results to GOLDEN_EVAL.md.

Run: uv run python exercises/04_golden_set_eval.py
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class GoldenCase:
    question: str
    relevant_doc_ids: list[str]  # ids in your corpus


# TODO: define 20 cases for your domain
GOLDEN_SET: list[GoldenCase] = [
    # GoldenCase(question="...", relevant_doc_ids=["doc_id_1"]),
]


def mrr(retrieved_ids: list[str], relevant_ids: list[str]) -> float:
    """Mean Reciprocal Rank for a single query."""
    # TODO: find position of first relevant doc in retrieved list
    # MRR = 1 / position (1-indexed), or 0 if not found
    raise NotImplementedError


def recall_at_k(retrieved_ids: list[str], relevant_ids: list[str], k: int) -> float:
    """Recall@k for a single query."""
    # TODO: |retrieved[:k] ∩ relevant| / |relevant|
    raise NotImplementedError


def run_eval(retrieval_fn: object) -> dict:
    """Run full golden set evaluation. Returns metrics dict."""
    # TODO: for each GoldenCase:
    #   retrieved = retrieval_fn(case.question, k=10)
    #   compute recall@1, recall@5, mrr
    # Return mean over all cases
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: plug in your retrieval function (hybrid or vector)
    # metrics = run_eval(your_retrieval_fn)
    # print metrics table
    # write to GOLDEN_EVAL.md
    pass
