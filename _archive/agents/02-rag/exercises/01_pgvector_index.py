"""Exercise 01 — Index corpus in pgvector and query by similarity.

Goal: understand vector search at the DB level before abstracting it.
  1. Create a pgvector table with embedding column.
  2. Embed a list of text chunks with OpenAI embeddings API.
  3. Insert chunks + embeddings into Postgres.
  4. Query top-k nearest neighbors for a question.
  5. Print results with similarity score.

Run: uv run python exercises/01_pgvector_index.py
"""

from __future__ import annotations

import os

# psycopg3 + pgvector
# from pgvector.psycopg import register_vector

SAMPLE_DOCS = [
    "Consultas podem ser agendadas pelo WhatsApp ou pelo app.",
    "O horário de funcionamento é de segunda a sexta, das 8h às 18h.",
    "Aceitamos convênios: Bradesco, Amil, Unimed e SulAmérica.",
    "Para cancelar, ligue com pelo menos 24 horas de antecedência.",
    "Exames laboratoriais devem ser retirados em até 7 dias.",
]


def embed(texts: list[str]) -> list[list[float]]:
    """Return embeddings for each text using OpenAI API."""
    # TODO: call openai.embeddings.create(model="text-embedding-3-small", input=texts)
    # return list of embedding vectors
    raise NotImplementedError


def create_table(conn: object) -> None:
    """Create docs table with pgvector column if not exists."""
    # TODO: CREATE TABLE IF NOT EXISTS docs
    #   (id SERIAL PRIMARY KEY, content TEXT, embedding vector(1536))
    raise NotImplementedError


def insert_docs(conn: object, docs: list[str], embeddings: list[list[float]]) -> None:
    """Insert docs and their embeddings."""
    # TODO: bulk insert
    raise NotImplementedError


def search(conn: object, query: str, k: int = 5) -> list[dict]:
    """Return top-k docs by cosine similarity to query."""
    # TODO: embed query, then:
    # SELECT content, 1 - (embedding <=> %s) AS similarity
    # FROM docs ORDER BY embedding <=> %s LIMIT %s
    raise NotImplementedError


if __name__ == "__main__":
    DATABASE_URL = os.environ["DATABASE_URL"]
    # TODO: connect, create_table, insert_docs, search("Como cancelo minha consulta?")
