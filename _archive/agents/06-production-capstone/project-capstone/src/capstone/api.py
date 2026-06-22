"""FastAPI entrypoint for the capstone system."""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Capstone Agent")


class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    reply: str
    session_id: str
    sources: list[str] = []


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    # TODO: wire up multi-agent system
    raise NotImplementedError


@app.get("/health")
async def health() -> dict:
    # TODO: check DB, Langfuse, MCP server
    raise NotImplementedError
