# AI Agents Lab

Learning workspace for production-grade AI agents. See `AI_AGENTS_ROADMAP.md` for full context.

## Progress

- [ ] 00 — Foundations: ReAct from scratch
- [ ] 01 — Agent Anatomy: production single-agent
- [ ] 02 — RAG: hybrid search + retrieval evals
- [ ] 03 — Orchestration: LangGraph multi-agent
- [ ] 04 — MCP: FastMCP server + consumer
- [ ] 05 — Eval & Observability: Langfuse + regression suite
- [ ] 06 — Production Capstone: full system on VPS

## Ordem

00 → 01 → 02 → 03 obrigatória. 04 e 05 são aceleradores de contratação — não deixe pro fim.

## Stack

Python + uv. Each stage is independent `uv` project.

```bash
cd <stage>/project-*/
uv sync
uv run pytest
```
