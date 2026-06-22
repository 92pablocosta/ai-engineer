"""Exercise 01 — Persistent memory with SQLite.

Goal: add cross-session memory to an agent.
  1. Create a SQLite table to store conversation history.
  2. Load history at session start, append each turn, persist after each turn.
  3. Implement session_id so multiple users don't share history.
  4. Add a "forget" command that clears a session.

Run: uv run python exercises/01_persistent_memory.py
"""

from __future__ import annotations

import sqlite3
import uuid
from dataclasses import dataclass
from typing import Any


DB_PATH = "memory.db"


@dataclass
class Message:
    role: str  # "user" | "assistant"
    content: str
    session_id: str


class MemoryStore:
    """SQLite-backed conversation history."""

    def __init__(self, db_path: str = DB_PATH) -> None:
        self.db_path = db_path
        # TODO: create table if not exists:
        # CREATE TABLE IF NOT EXISTS messages
        #   (id INTEGER PRIMARY KEY, session_id TEXT, role TEXT, content TEXT, created_at TIMESTAMP)

    def load(self, session_id: str) -> list[Message]:
        """Load all messages for a session, ordered by creation time."""
        # TODO: implement
        raise NotImplementedError

    def append(self, message: Message) -> None:
        """Persist a single message."""
        # TODO: implement
        raise NotImplementedError

    def clear(self, session_id: str) -> None:
        """Delete all messages for a session."""
        # TODO: implement
        raise NotImplementedError


def chat_with_memory(session_id: str, user_input: str, store: MemoryStore) -> str:
    """One turn of a conversation with persistent memory."""
    # TODO:
    # 1. Load history for session_id
    # 2. Append new user message
    # 3. Build messages list for LLM (system + history + new message)
    # 4. Call LLM
    # 5. Append assistant response to store
    # 6. Return response text
    raise NotImplementedError


if __name__ == "__main__":
    store = MemoryStore()
    session = str(uuid.uuid4())
    print("Session:", session)
    while True:
        user = input("You: ")
        if user.lower() == "forget":
            store.clear(session)
            print("[Memory cleared]")
            continue
        response = chat_with_memory(session, user, store)
        print(f"Agent: {response}")
