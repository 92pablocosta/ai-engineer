"""Exercise 02 — Hybrid search: BM25 + vector.

Goal: understand why hybrid beats pure vector for keyword-heavy queries.
  1. Implement BM25 scoring (use rank_bm25 library or pg full-text search).
  2. Combine BM25 rank + vector similarity rank (Reciprocal Rank Fusion is simple).
  3. Run same 5 queries on pure vector vs hybrid, compare results.
  4. Record which approach returns the correct doc for each query.

Run: uv run python exercises/02_hybrid_search.py
"""

from __future__ import annotations

TEST_QUERIES = [
    "cancelar consulta",
    "horário de atendimento",
    "convênios aceitos",
    "retirar exame",
    "agendar pelo whatsapp",
]

# expected_doc_index: which SAMPLE_DOCS (from ex01) is the correct answer for each query
EXPECTED: list[int] = [3, 1, 2, 4, 0]


def bm25_search(query: str, corpus: list[str], k: int = 5) -> list[int]:
    """Return indices of top-k docs by BM25 score."""
    # TODO: use rank_bm25.BM25Okapi or implement Postgres full-text search
    raise NotImplementedError


def vector_search(query: str, conn: object, k: int = 5) -> list[int]:
    """Return indices of top-k docs by vector similarity."""
    # TODO: reuse logic from ex01
    raise NotImplementedError


def reciprocal_rank_fusion(
    rankings: list[list[int]], k: int = 60
) -> list[int]:
    """Merge multiple ranked lists into one via RRF."""
    # TODO: score = sum(1 / (k + rank_in_list_i)) for each doc
    raise NotImplementedError


def recall_at_1(results: list[int], expected: int) -> int:
    """Return 1 if expected is in top-1 result, else 0."""
    return 1 if results and results[0] == expected else 0


if __name__ == "__main__":
    # TODO: run both approaches on TEST_QUERIES, print recall@1 comparison table
    pass
