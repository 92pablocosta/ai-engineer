"""Document ingestion: chunk → embed → store in pgvector."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Chunk:
    doc_id: str
    chunk_id: str
    content: str
    metadata: dict


def load_documents(corpus_dir: Path) -> list[dict]:
    """Load raw documents from directory. Returns list of {id, content, path}."""
    # TODO: support .txt, .md, .pdf (basic text extraction)
    raise NotImplementedError


def chunk_document(doc: dict, chunk_size: int = 512, overlap: int = 64) -> list[Chunk]:
    """Recursive character splitting. Return list of Chunk."""
    # TODO: implement recursive split on ["\n\n", "\n", " ", ""]
    raise NotImplementedError


def embed_chunks(chunks: list[Chunk]) -> list[list[float]]:
    """Batch embed chunk contents with OpenAI API."""
    # TODO: batch in groups of 100 to avoid rate limits
    raise NotImplementedError


def store_chunks(conn: object, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
    """Upsert chunks into Postgres (pgvector)."""
    # TODO: CREATE TABLE IF NOT EXISTS chunks
    #   (chunk_id TEXT PRIMARY KEY, doc_id TEXT, content TEXT,
    #    metadata JSONB, embedding vector(1536))
    # Upsert on chunk_id (re-indexing same doc = update, not duplicate)
    raise NotImplementedError


def main(corpus_dir: str) -> None:
    """CLI entrypoint: index all documents in corpus_dir."""
    # TODO: load → chunk → embed → store
    # Print: N docs, M chunks indexed
    raise NotImplementedError


if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "data/corpus")
