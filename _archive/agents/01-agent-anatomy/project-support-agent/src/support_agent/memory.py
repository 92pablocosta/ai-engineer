"""Postgres-backed session memory."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Turn:
    role: str  # "user" | "assistant"
    content: str


class SessionMemory:
    """Persist conversation turns per session in Postgres."""

    def __init__(self, dsn: str) -> None:
        self.dsn = dsn
        # TODO: create psycopg connection pool
        # TODO: CREATE TABLE IF NOT EXISTS turns
        #   (id SERIAL PRIMARY KEY, session_id TEXT, role TEXT, content TEXT, created_at TIMESTAMPTZ DEFAULT now())

    async def load(self, session_id: str) -> list[Turn]:
        """Return all turns for session, ordered by created_at."""
        # TODO: implement
        raise NotImplementedError

    async def append(self, session_id: str, turn: Turn) -> None:
        """Persist a turn."""
        # TODO: implement
        raise NotImplementedError

    async def clear(self, session_id: str) -> None:
        """Delete all turns for a session."""
        # TODO: implement
        raise NotImplementedError

    async def health_check(self) -> bool:
        """Return True if DB connection is alive."""
        # TODO: SELECT 1
        raise NotImplementedError
