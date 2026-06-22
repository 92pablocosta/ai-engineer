"""Reusable evaluation helpers shared across stages.

Recall@k, MRR, nDCG for retrieval.
LLM-as-judge scaffolding.
Golden dataset loader/writer.
"""

from __future__ import annotations

from typing import Any

# TODO: implement
# recall_at_k(retrieved: list[str], relevant: list[str], k: int) -> float
# mrr(retrieved: list[str], relevant: list[str]) -> float
# ndcg_at_k(retrieved: list[str], relevant: list[str], k: int) -> float
# load_golden_dataset(path: str) -> list[dict]
# save_golden_dataset(cases: list[dict], path: str) -> None
# llm_judge_score(output: str, rubric: str, llm_client: Any) -> dict
#   returns: {"score": int, "reasoning": str, "axes": dict}
