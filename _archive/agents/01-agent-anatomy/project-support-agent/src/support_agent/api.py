"""FastAPI entrypoint."""

from __future__ import annotations

import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from support_agent.agent import SupportAgent
from support_agent.memory import SessionMemory

app = FastAPI(title="Support Agent")

# TODO: init memory and agent on startup (use lifespan context manager)


class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    reply: str
    session_id: str


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    # TODO: call agent.chat(req.session_id, req.message)
    # Catch GuardrailViolation → return 422 with useful message
    # Catch unexpected exceptions → log + return 500 with generic message
    raise NotImplementedError


@app.get("/health")
async def health() -> dict:
    # TODO: check DB connectivity via memory.health_check()
    # return {"status": "ok", "db": "ok"} or {"status": "degraded", "db": "error"}
    raise NotImplementedError
