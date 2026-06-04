# System Design Questions — Agentic Systems

Practice drawing these on paper (or whiteboard). The answer is never one diagram — it's trade-offs.

---

## 1. Design a customer support agent for a telecom company

**What they're testing**: multi-agent architecture, guardrails, escalation, cost management.

Sketch:
- Entry point (FastAPI / WhatsApp webhook)
- Intent classifier (cheap model — Haiku)
- Routing: FAQ → RAG agent, Account actions → specialist agent + human approval gate
- Memory: session (Redis) + long-term (Postgres)
- Observability: Langfuse trace per session
- Guardrail layer: PII + unauthorized action detection

Trade-offs to mention:
- Why Haiku for intent classification, not Opus? (cost: ~100x cheaper, sufficient for classification)
- Why not one big agent? (latency, cost, debuggability — specialized agents fail independently)
- How do you handle escalation? (interrupt_before in LangGraph, ticket system webhook)

---

## 2. Design a RAG system over 1M legal documents

**What they're testing**: chunking strategy, retrieval architecture, eval.

Sketch:
- Ingestion pipeline: PDF → text extract → recursive chunk (512 tokens, 64 overlap)
- pgvector + BM25 hybrid search + Cohere Rerank
- Agent that decides if context is sufficient (re-retrieves with query rewrite if not)
- Golden set of 100 questions with recall@k baseline

Trade-offs to mention:
- Why hybrid over pure vector? (technical terms have low semantic similarity — BM25 catches exact matches)
- Why 512 chunks, not 2048? (larger chunks reduce precision; smaller chunks lose context)
- How would you scale beyond 1M docs? (Qdrant sharding, async ingestion pipeline, embedding cache)

---

## 3. How would you detect and respond to a quality regression after a prompt change?

**What they're testing**: eval maturity, CI/CD integration.

Answer:
- Golden dataset checked into git (versioned as test data)
- LLM judge rubric with explicit anchors (not vibes)
- Regression runner as CI step: PR that changes any prompt must pass eval gate
- Langfuse dashboards: p50/p95 judge score + success_rate trend over time
- Canary: route 5% of prod traffic to new prompt, compare metrics before full rollout

---

## 4. A client asks for a multi-agent system where agents collaborate on a document. How do you design state management?

**What they're testing**: LangGraph state, reducers, checkpoints.

Answer:
- AgentState TypedDict with explicit fields (research_notes, draft, review_feedback, approved)
- Annotated[list, operator.add] for messages (append-only log, never overwrite)
- SqliteSaver/PostgresSaver for durable execution (process restart = resume from checkpoint)
- Human-in-the-loop: interrupt_before=[approval_node] — graph pauses, waits for external event
- Each worker updates its own state slice; supervisor reads all slices to route

---

## 5. How do you prevent prompt injection in a public-facing agent?

**What they're testing**: security awareness (OWASP LLM Top 10).

Answer:
- Input sanitization: detect "ignore previous instructions", "you are now X", jailbreak patterns
- System prompt hardening: explicit persona + instruction anchoring + output format constraints
- Tool call validation: agent cannot call tools with arbitrary strings — all tool inputs validated against Pydantic schema
- Output filtering: LLM output passes through PII guard + code execution guard before reaching user
- Monitoring: Langfuse flags unusual tool call patterns (same tool > N times, unexpected tool combos)
