"""Exercise 03 — Reranking and measuring recall@5 improvement.

Goal: show that reranking reduces noise in top-k retrieval.
  1. Retrieve top-10 candidates from hybrid search.
  2. Rerank with Cohere Rerank or a local cross-encoder.
  3. Measure recall@5 before and after reranking.
  4. Print: recall@5 without rerank vs with rerank.

Run: uv run python exercises/03_reranking.py
"""

from __future__ import annotations

from typing import Any


def cohere_rerank(query: str, docs: list[str], top_n: int = 5) -> list[int]:
    """Return indices of top_n docs after Cohere reranking."""
    # TODO: import cohere, call co.rerank(query=query, documents=docs, top_n=top_n)
    # extract .results[i].index
    raise NotImplementedError


def recall_at_k(retrieved_indices: list[int], relevant_indices: list[int], k: int) -> float:
    """Recall@k = |retrieved[:k] ∩ relevant| / |relevant|."""
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    # TODO:
    # 1. For each query in golden set (from ex04 or hardcode a few):
    #    - get top-10 via hybrid_search
    #    - compute recall@5 WITHOUT reranking
    #    - rerank, compute recall@5 WITH reranking
    # 2. Print comparison: query | recall@5 before | recall@5 after
    pass
