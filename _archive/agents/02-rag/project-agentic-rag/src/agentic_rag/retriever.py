"""Hybrid retrieval: BM25 + vector similarity + Cohere reranking."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SearchResult:
    chunk_id: str
    doc_id: str
    content: str
    score: float


def vector_search(conn: object, query: str, k: int = 10) -> list[SearchResult]:
    """Cosine similarity search via pgvector."""
    # TODO: embed query, SELECT top-k by <=> distance
    raise NotImplementedError


def bm25_search(query: str, corpus_chunks: list[dict], k: int = 10) -> list[SearchResult]:
    """BM25 keyword search over in-memory corpus."""
    # TODO: use rank_bm25.BM25Okapi
    raise NotImplementedError


def reciprocal_rank_fusion(
    *rankings: list[SearchResult], k: int = 60
) -> list[SearchResult]:
    """Merge ranked lists via RRF. Higher score = better rank."""
    # TODO: implement RRF scoring, return merged + sorted list
    raise NotImplementedError


def rerank(query: str, results: list[SearchResult], top_n: int = 5) -> list[SearchResult]:
    """Rerank top-k results with Cohere Rerank API."""
    # TODO: co.rerank(), map back to SearchResult
    raise NotImplementedError


def retrieve(
    conn: object,
    query: str,
    corpus_chunks: list[dict],
    top_k: int = 10,
    rerank_top_n: int = 5,
) -> list[SearchResult]:
    """Full pipeline: hybrid search → RRF → rerank."""
    # TODO: vector_search + bm25_search → RRF → rerank
    raise NotImplementedError
