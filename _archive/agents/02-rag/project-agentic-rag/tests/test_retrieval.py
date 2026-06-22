"""Tests for retrieval pipeline."""

from __future__ import annotations

import pytest

from agentic_rag.retriever import reciprocal_rank_fusion, SearchResult


class TestRRF:
    def test_higher_rank_gets_higher_score(self) -> None:
        # TODO: doc ranked #1 in both lists should outscore doc ranked #5 in both
        pytest.skip("not implemented")

    def test_deduplicates_docs(self) -> None:
        # TODO: same chunk_id in multiple rankings should appear once in output
        pytest.skip("not implemented")


class TestRecallAtK:
    def test_perfect_retrieval(self) -> None:
        # TODO: import recall_at_k from eval_utils, assert recall_at_k([0,1,2],[0,1,2],3)==1.0
        pytest.skip("not implemented")

    def test_zero_recall(self) -> None:
        # TODO: assert recall_at_k([3,4,5],[0,1,2],3)==0.0
        pytest.skip("not implemented")
