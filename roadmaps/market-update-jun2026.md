# Market Update — AI/LLM Engineer (Jun 2026)

> Verified against live job market data. Cross-references original roadmap `roadmap-ai-engineer-pablo-2026.md`.
> Research date: 2026-06-04.

---

## TL;DR — What Changed

| Topic | Roadmap Said | Market Reality |
|---|---|---|
| Freelance entry rate | US$30–40/hr | US$75–125/hr (junior via direct) / US$45–60/hr (Lemon.io) |
| Mid contract rate | US$65–95/hr | US$125–175/hr (direct) / US$55–81/hr (Lemon.io) |
| Eval stack (RAGAS + DeepEval) | Current | ✅ Still dominant, no change |
| Raw API > LangChain | Correct | ✅ Validated — LangChain roles pay ~$80K less at top end |
| MCP = 2026 skill | Correct | ✅ 8,400+ open roles requiring MCP skills |
| Agent framework | LangGraph only | ⚠️ Add Claude Agent SDK + OpenAI Agents SDK |
| Specialization pressure | "Decide later" | ⚠️ Pick now — 75%+ postings require domain specialization |

---

## 1. Salary & Rate Reality (2026)

### Freelance / Contract Hourly (USD)

**Via Lemon.io** (most realistic entry point for non-US devs):

| Level | Range | Median |
|---|---|---|
| Mid (2–5 yrs) | $27–60/hr | $45/hr |
| Senior (5–8 yrs) | $35–94/hr | $55/hr |
| Strong Senior (8+ yrs) | $50–105/hr | $81/hr |
| LLM specialist | $37–58/hr | ~$48/hr |

> Pablo's entry target on Lemon.io: **$45–55/hr** (mid, AI/LLM specialist with prod evidence).

**Direct US contracts** (Upwork, direct outreach, Braintrust):

| Level | Range |
|---|---|
| Junior | $75–125/hr |
| Mid | $125–175/hr |
| Senior | $175–250/hr |
| RAG specialist | $150–250/hr |
| AI agent specialist | $175–300/hr |

> Upwork median: $150/hr. Toptal/Turing: $220–240/hr.

**Specialization premiums (2026):**
1. AI agent development: +$175–300/hr range
2. RAG implementation: +$150–250/hr range
3. LLM API integration: +$125–200/hr range

LLM specialists add **+30–50%** to baseline rates.

### Full-Time Remote (annual, USD)

| Level | Range |
|---|---|
| Entry (AI/LLM focus) | $125–180K |
| Mid | $170–260K |
| Senior specialist | $200–312K |

> Entry at top AI companies (Anthropic, OpenAI, Pinecone): $125–180K base.

### Brazil Context

- Brazil nearshore rate (agencies): $25–90/hr depending on seniority
- Pablo has advantage: native English + prod AI + Australian background = can target direct US rates, not nearshore rates

---

## 2. Skills Demand — What's Verified Hot

**RAG appears in 65% of applied LLM job listings.** Not slowing.

Top 10 skills replacing "LangChain + Pinecone on resume":
1. Agent orchestration
2. MCP integration ← Pablo already has MCP server built
3. Eval design (RAGAS/DeepEval)
4. Prompt engineering
5. Vector DB / RAG production
6. Cost optimization / multi-provider routing
7. Safety / guardrails
8. Computer-use deployment
9. Production observability (Langfuse, LangSmith)
10. Frontier model fluency (API-level, not wrapper)

**Python in 71% of job postings.** Table stakes.

---

## 3. Eval Stack — No Change Needed

RAGAS + DeepEval still dominant production pattern in 2026.

| Tool | Role | Status |
|---|---|---|
| RAGAS | Reference metrics, golden dataset gen, RAG-specific (faithfulness, context precision/recall, answer relevancy) | ✅ Active, reference standard |
| DeepEval | CI/CD integration, pytest-style, build fails on metric drop | ✅ Active, most production GenAI QA programs |
| Langfuse | Tracing, token/cost/latency, self-hostable | ✅ Still go-to for self-hosted |

**Pattern:** RAGAS → explore + build golden set. DeepEval → CI gate. Langfuse → prod tracing. No change from roadmap.

---

## 4. Framework Landscape — Update Required

### What roadmap said
LangGraph in Phase 6. Nothing else.

### What market shows

**LangChain:** Still 34% of job listings by volume BUT pays ~$80K less at top end than framework-agnostic roles. Red flag in senior interviews.

**Raw API / vendor SDKs (winning):**
- **Claude Agent SDK** — fastest growing for Anthropic-native agents (late 2025–2026)
- **OpenAI Agents SDK** — production-mature, deeper Platform integration
- Both absorbed core LangChain abstractions (memory, tool use, retrieval)

**LangGraph:** Still valid for stateful workflows with loop/branch/decision. Keep in Phase 6.

### Updated Phase 6 stack
```
Raw loop (already know from Phase 2)
  └─ LangGraph — stateful workflows, human-in-loop
  └─ Claude Agent SDK — Anthropic-native production agents
  └─ OpenAI Agents SDK — OpenAI-native production agents
```

---

## 5. Specialization — Pick Now, Not at Graduation

**Roadmap:** "Decide focus (RAG vs agentic) at medium-term."

**Market reality:** 75%+ of 2026 postings require domain specialization. Generalists screened before first interview. Specialists command **30–50% salary premium**.

### Decision framework for Pablo

| Path | Pablo's current edge | Market demand |
|---|---|---|
| **RAG / Retrieval** | DentBot prod data, VishPath use case | 65% of LLM listings, $150–250/hr specialist rate |
| **Agentic / Orchestration** | MCP server already built | Fastest growing, $175–300/hr specialist rate |

**Recommendation:** RAG first (closes biggest interview gap, Phases 3–4 already on that path). Agentic second (MCP head start). Frame narrative as "RAG-specialist who also builds agents" — not a generalist.

---

## 6. Study Sequence — No Change to Critical Path

Phases 1→4 unchanged. Eval-first principle unchanged.

```
Phase 0  Python basics          (parallel, 1–2w)
Phase 1  FastAPI prod-grade     (1–2w)
Phase 2  Raw LLM API + agent    (1–2w)
Phase 3  RAG from scratch       (2–3w)  ← specialization starts here
Phase 4  Eval ⭐                (1w)    ← closes biggest interview gap
Phase 5  Observability+guards   (1w)
Phase 6  LangGraph + Claude/OAI Agent SDK + multi-agent  (medium)
Phase 7  Cost optim + cloud     (medium)
```

---

## 7. Updated Income Targets

### Short term (now → Aug 2026)

| Channel | Old target | Updated target |
|---|---|---|
| Annotation (Outlier etc) | Pipeline active | Unchanged |
| Lemon.io / Upwork freelance | US$30–40/hr | US$45–60/hr (Lemon.io) / US$75–100/hr (direct Upwork) |
| Direct client (DentBot proof) | US$30–40/hr | US$60–80/hr (direct, small SMB) |

### Medium term (contract, remote)

| Profile | Target rate |
|---|---|
| Mid LLM/RAG (direct US contract) | US$125–150/hr |
| Mid LLM/RAG (Lemon.io / Braintrust) | US$55–70/hr |
| RAG specialist with metrics | US$150–175/hr |

---

## 8. What to Add to Portfolio NOW

Based on what 2026 interviewers actually ask:

1. **README with numbers** — recall@10, faithfulness score, p50/p95 latency, retrieval hit rate. Not "I built a RAG." Numbers or it didn't happen.
2. **Failure mode documentation** — what broke, how you measured it, how you fixed it. This is the question that separates mid from junior in every interview.
3. **Claude Agent SDK example** — small but shows frontier model fluency beyond "used ChatGPT API".
4. **Cost reduction %** — any project. "Reduced inference cost 40% via caching + model routing" beats any tech stack list.

---

## Sources

- [Freelance AI Developer Hourly Rate 2026 | Second Talent](https://www.secondtalent.com/resources/freelance-ai-developer-hourly-rate-2026/)
- [Freelance LLM Developer Hourly Rate 2026 | Second Talent](https://www.secondtalent.com/resources/freelance-llm-developer-hourly-rate-us/)
- [AI Engineers Salary 2026 by Seniority | Lemon.io](https://lemon.io/rate-calculator/ai-engineers/)
- [Lemon.io: AI Engineers Out-Earn Traditional Devs by 41% | TechBullion](https://techbullion.com/lemon-io-report-reveals-ai-engineers-out-earn-traditional-developers-by-up-to-41-percent/)
- [AI Engineer Compensation 2026 | Axiom Recruit](https://www.axiomrecruit.com/resources/industry-insights/ai-engineer-compensation-2026--what-the-world-is-paying/)
- [Top 10 Most In-Demand AI Engineering Skills 2026 | Second Talent](https://www.secondtalent.com/resources/most-in-demand-ai-engineering-skills-and-salary-ranges/)
- [AI Developer Hiring 2026: Skills That Actually Matter | Digital Applied](https://www.digitalapplied.com/blog/ai-developer-hiring-skills-that-matter-2026)
- [RAG Evaluation Frameworks 2026 | CallSphere](https://callsphere.ai/blog/rag-evaluation-frameworks-2026-ragas-trulens-deepeval)
- [RAGAS, TruLens, DeepEval Compared 2026 | Atlan](https://atlan.com/know/llm-evaluation-frameworks-compared/)
- [LangChain Exit: Raw SDK Migration 2026 | Ravoid](https://ravoid.com/blog/langchain-exit-raw-sdk-migration-2026)
- [LangChain vs CrewAI vs Raw API 2026 | AI Builder Club](https://www.aibuilderclub.com/blog/langchain-vs-crewai-vs-raw-api)
- [Agentic AI Engineers Most In-Demand 2026 | AI Staffing Ninja](https://www.aistaffingninja.com/blog/beyond-llms-agentic-ai-engineers/)
- [Brazil Software Engineer Salary 2026 | Howdy](https://www.howdy.com/blog/brazil-software-engineer-salary-hiring-cost-benchmarks)
- [RAG Engineer Jobs 2026 | PropelGrad](https://propelgrad.com/ai-jobs/rag-engineer)
