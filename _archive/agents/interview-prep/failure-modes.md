# Failure Modes in Production Agentic Systems

Fill this in as you build each project. These are THE senior-level interview question.
Format: symptom → root cause → mitigation → how you'd detect it.

---

## Stage 00 — ReAct Agent

### [Fill in after building]

**Symptom**:  
**Root cause**:  
**Mitigation**:  
**Detection**:  

---

## Stage 01 — Support Agent

### [Fill in after building]

---

## Stage 02 — RAG

### Retrieval silently returns wrong chunks

**Symptom**: Agent gives plausible but wrong answers. Users don't always notice.  
**Root cause**: Embedding model drift, or corpus updated without re-indexing.  
**Mitigation**: Regression suite on golden set runs nightly. Alert if recall@5 drops > 5%.  
**Detection**: Langfuse trace shows retrieved chunk_ids → check if correct.

### [Add more as you find them]

---

## Stage 03 — LangGraph Multi-Agent

### Tool-call retry loop

**Symptom**: Agent keeps calling the same failing tool. Tokens and cost spiral.  
**Root cause**: No max_retries on tool errors; agent interprets error as "try harder."  
**Mitigation**: Per-tool retry limit; circuit breaker after N consecutive failures.  
**Detection**: Langfuse trace shows same tool called > 3 times in one session.

### State explosion on long sessions

**Symptom**: Context window hit, agent loses early context, wrong decisions.  
**Root cause**: messages list grows unbounded; no summarization or truncation strategy.  
**Mitigation**: Summarize messages older than N turns. Keep important state in typed fields.  
**Detection**: Monitor input_tokens per session; alert above threshold.

### [Add more]

---

## Stage 04 — MCP

### [Fill in after building]

---

## Stage 05 — Eval

### LLM judge score inflation

**Symptom**: Judge gives 3/3 to bad responses. Regression suite always passes.  
**Root cause**: Rubric too vague; judge optimizes for "positive" outputs.  
**Mitigation**: Explicit anchors for each score level; test judge on known-bad examples.  
**Detection**: Manually sample 10% of judge outputs; compare with human labels.

---

## Stage 06 — Capstone

### [Fill in after building]

---

## Cross-cutting

### Prompt regression after model upgrade

**Symptom**: Behavior changes after upgrading claude-sonnet-4-5 → 4-6. Regression suite not catching it.  
**Root cause**: New model interprets prompts differently; old eval threshold too loose.  
**Mitigation**: Pin model versions in prod; run A/B eval before upgrading; tighten eval thresholds.  
**Detection**: Regression suite with strict thresholds runs on model change PR.
