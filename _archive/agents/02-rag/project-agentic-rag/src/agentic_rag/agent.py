"""Agentic RAG — agent decides when to search, re-searches if context insufficient."""

from __future__ import annotations

import sys

from agentic_rag.retriever import SearchResult, retrieve


def format_context(results: list[SearchResult]) -> str:
    """Format search results as LLM context with citations."""
    # TODO: format as "[doc_id chunk_id] content" for each result
    raise NotImplementedError


class RAGAgent:
    def __init__(self, conn: object, corpus_chunks: list[dict]) -> None:
        self.conn = conn
        self.corpus_chunks = corpus_chunks
        # TODO: init LLM client

    def answer(self, question: str) -> dict:
        """Answer question with source citations. Returns {answer, sources}."""
        # TODO:
        # 1. Initial retrieve
        # 2. Ask LLM: is context sufficient? If not, re-retrieve with refined query
        # 3. Generate answer grounded in context
        # 4. Extract citations from answer
        # 5. Return {answer, sources: list of chunk_ids used}
        raise NotImplementedError


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "What is this about?"
    # TODO: connect DB, load corpus_chunks, run agent.answer(question)
