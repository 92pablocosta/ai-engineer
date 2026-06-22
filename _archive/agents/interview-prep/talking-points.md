# Talking Points — How to Narrate Each Project

Format per project: business problem → your solution → what you measured → what you learned.
Write in English. You're fluent — use it. It's a differentiator for international roles.

---

## Stage 00 — ReAct Agent from Scratch

**Draft (fill in after building):**

"Before using any orchestration framework, I built a ReAct agent from scratch — just the Anthropic SDK and Python. The goal was to understand what happens underneath LangGraph. I implemented the Reason→Act→Observe loop manually, with a configurable iteration limit to prevent runaway costs, structured logging of every step, and per-execution token cost tracking. The insight I brought into my framework work is that LangGraph's value is state management and durable execution — the loop itself is straightforward once you've written it by hand."

---

## Stage 01 — Support Agent + FastAPI

**Draft:**

"I built a single-domain support agent deployed as a FastAPI service on my VPS. The agent handles scheduling queries for a clinic — checking availability, creating reminders, escalating to human when needed. I added Postgres-backed session memory so context persists across messages, and output guardrails that block PII from reaching users and require explicit confirmation for destructive actions like cancellation. The key decision was designing guardrails as a separate layer — not inside the agent logic — so they're testable independently and easy to audit."

---

## Stage 02 — Agentic RAG

**Draft:**

"For the RAG stage, I built a system over [your corpus] and measured it. Pure vector search gave me [X]% recall@5. Hybrid search — BM25 combined with vector via Reciprocal Rank Fusion — improved it to [Y]%. Adding Cohere Rerank on top brought it to [Z]%. The numbers are in the EVAL.md. The agentic piece is that the agent decides whether to search at all, and re-searches with a refined query if the first retrieval doesn't give enough context. Responses always include the source chunk ID, so hallucinations are traceable."

---

## Stage 03 — Multi-Agent with LangGraph

**Draft:**

"I built a supervisor/worker multi-agent system in LangGraph: a supervisor routes tasks between a researcher, a writer, and a reviewer. State is typed with TypedDict and persists to SQLite via LangGraph checkpoints — the system survives process restarts. I added a human-in-the-loop gate before final delivery: the graph pauses, waits for approval, then resumes. I also built the same agent in Pydantic AI and the Anthropic SDK to form a real opinion. LangGraph wins when you need durable state and human-in-the-loop — the overhead is worth it. Pydantic AI wins when type safety matters more than built-in persistence."

---

## Stage 04 — MCP Server

**Draft:**

"I built a FastMCP server that exposes my RAG pipeline as an MCP service — tools for searching the knowledge base and adding documents, plus a resource endpoint for corpus stats. A LangGraph agent connects to it via HTTP/SSE and discovers available tools at runtime through the MCP protocol. The key point is that the agent has no direct import of the server code — it goes through the protocol. This is the difference between a tool and an MCP tool: MCP lets any client use it, not just the one you built it for."

---

## Stage 05 — Eval Pipeline

**Draft:**

"This stage is where my annotation background became an engineering asset. I instrumented the support agent with Langfuse self-hosted on my VPS, so every LLM call and tool execution is a searchable span. I built a golden dataset of [N] cases, tagged by type: happy path, edge cases, guardrail tests, multi-step flows. The LLM judge has explicit rubrics with score anchors — I learned from my annotation work that 'feels right' doesn't scale, you need defined criteria per axis. The regression suite exits with code 1 if the pass rate drops below 80%, so any prompt change that regresses quality fails before it ships."

---

## Stage 06 — Capstone

**Draft (fill in after building):**

"The capstone brings everything together: [describe your domain]. Multi-agent LangGraph system with RAG over [corpus], exposed via a FastMCP server, all instrumented with Langfuse. The system is deployed on my VPS with Docker and Traefik. What I'm most proud of is the eval pipeline — I can show you a Langfuse trace and point to exactly where a response failed and why. The README documents 5 known failure modes and their mitigations. I didn't build this to be a demo; I built it to be a service I could hand to a client."
