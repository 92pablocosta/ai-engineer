"""Tests for MCP server tools."""

from __future__ import annotations

import pytest


class TestSearchKnowledge:
    def test_returns_results(self) -> None:
        # TODO: start server as subprocess, connect client, call search_knowledge
        # assert results is a list with content
        pytest.skip("not implemented")

    def test_empty_query_returns_error(self) -> None:
        pytest.skip("not implemented")


class TestCorpusStats:
    def test_resource_readable(self) -> None:
        # TODO: client.read_resource("rag://corpus/stats") returns valid JSON
        pytest.skip("not implemented")
