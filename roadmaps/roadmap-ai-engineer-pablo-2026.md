# Roadmap AI Engineer — Pablo Costa (2026)

> Posicionamento-base: **AI/LLM Application Engineer com produção real**, não "Python dev júnior".
> O mercado júnior genérico encolheu; o de AI/LLM application engineer cresceu. Você entra na fila certa.
>
> *v2 — inclui sequência de estudo por dependência técnica, stack de eval definido e glossário.*

---

## 0. Diagnóstico — onde você está hoje

**Já tem (acima da média de qualquer júnior):**
- LLM em produção com cliente pagante (DentBot — WhatsApp AI, n8n, Evolution API, OpenAI, PostgreSQL, Docker)
- Infra real: VPS Hostinger, Docker Compose, Traefik, Redis, Chatwoot
- MCP server construído (Research Assistant) — skill de 2026
- Inglês nativo (4 anos Austrália) → destrava mercado internacional
- Múltiplos deploys end-to-end (VishPath, Seraphina, landing pages)

**Gaps que derrubam em entrevista (ordem de prioridade):**
1. **Eval rigoroso** — nenhum projeto tem métrica (recall@10, faithfulness, hallucination rate). Maior buraco.
2. **RAG de produção** — falta UM projeto com retrieval medido, hybrid search, reranking, citations.
3. **Guardrails + observability explícitos** — PII redaction, prompt injection filter, trace IDs, métricas de token/latência.
4. **Profundidade de eng de software** — fechar fundamentos Python + um backend FastAPI sólido e testado.

---

## 1. Sequência de estudo — ordem por dependência técnica

> A ordem **não** é "do mais importante pro menos" — é dependência: cada fase é pré-requisito da seguinte. Cada uma termina com algo demonstrável. **A Fase 4 é onde o portfólio vira empregável.** Se precisar cortar caminho, corte na Fase 7, nunca na 4.

**Princípio que rege a ordem: fundamentals antes de framework.** Em 2026 o mercado trata "framework-dependent" (só sabe LangChain, não sabe o que ele faz por baixo) como red flag. Por isso você constrói o agent loop e o RAG **na mão primeiro**, e só introduz framework (LangGraph) onde ele paga — workflows com estado, loop e branching. Tentação a resistir: pular a Fase 2 porque "já uso OpenAI no DentBot". Usar a API dentro do n8n ≠ entender o loop a ponto de explicar tradeoffs em entrevista.

| Fase | O que estudar | Por quê / resultado | Duração |
|---|---|---|---|
| **0 — Python que basta** *(paralelo, não trave)* | funções, classes, `async/await`, type hints, Pydantic, `httpx`, deps (uv/venv), pytest básico | Não espere terminar o Curso em Vídeo pra avançar. O resto roda em background. | ~1–2 sem |
| **1 — FastAPI production-grade** | async, Pydantic models, dependency injection, error handling, rate limiting, testes | Esqueleto de todo projeto de produção; requisito recorrente nas vagas. *Resultado:* REST API testada e deployada na VPS. | ~1–2 sem |
| **2 — LLM na raça (raw API)** | agent loop (~60 linhas) com SDK OpenAI/Anthropic, tool-use, structured output (Pydantic), streaming, prompt engineering, embeddings | Separa quem entende de quem cola tutorial. *Resultado:* agente tool-calling que você entende 100%. | ~1–2 sem |
| **3 — RAG do zero → qualidade** | naive RAG no pgvector (ingestion/chunking → embeddings → retrieval → generation c/ citations); depois hybrid search (dense + BM25 + RRF), reranking (cross-encoder), query transformation | O que diferencia "chat-with-PDF de 15 min" de engenharia real. Construa já com golden set separado. *Resultado:* o RAG flagship rodando. | ~2–3 sem |
| **4 — Eval** ⭐ | RAGAS (faithfulness, context precision/recall, answer relevancy, recall@k) → DeepEval em CI/CD (pytest-style, falha o build se métrica cai) | **Fecha o maior gap.** É aqui que você responde "qual foi seu recall@10?". *Resultado:* README com números reais. | ~1 sem |
| **5 — Observability + guardrails** | Langfuse self-hosted na VPS (trace IDs, token/latência/custo); PII redaction, prompt injection filtering, context budget | *Resultado:* projeto com cara de produção, não de demo. | ~1 sem |
| **6 — Agentic + orchestration** *(médio prazo)* | LangGraph (loop/branch/decisão), multi-agente, integrar o MCP server, documentar **failure modes** | Framework onde paga. Failure modes = o que diferencia pleno de júnior. | médio prazo |
| **7 — Cost optimization + cloud** *(médio prazo)* | multi-provider routing c/ failover, caching, model selection; deploy AWS/GCP + CI/CD | Documentar economia em %. Vagas mid pedem cloud além da VPS. | médio prazo |

**Caminho crítico = Fases 1→4.** Tudo antes da 4 existe pra você chegar nela com algo real pra medir.

**Stack de eval (padrão de produção 2026, custo trivial — ~US$1 por run de 200 perguntas):**
- **RAGAS** — métricas RAG, leve, reference-free. Exploração + geração de golden dataset.
- **DeepEval** — eval como pytest. Roda no GitHub Actions; build falha se faithfulness < threshold.
- **Langfuse** — observability/tracing de produção, self-hostable (sobe na VPS).

---

## CURTO PRAZO — próximos 3 meses (jun → ago 2026)
**Objetivo:** tapar os 2 gaps que mais pesam (eval + RAG medido) e gerar renda em USD via contrato/freelance/annotation. *Cobre as Fases 0–5 da sequência acima.*

### Técnico (o que constrói portfólio empregável)
- [ ] **Projeto RAG flagship com métricas.** Pegue um domínio real (ex.: base jurídica do teu cliente de monitoramento, ou docs de imigração do VishPath). Stack: FastAPI + pgvector + embedding + reranking (cross-encoder) + citations obrigatórias.
  - [ ] Medir e documentar no README: **recall@10**, faithfulness, latência p50/p95, retrieval hit rate.
  - [ ] Implementar **hybrid search** (dense + BM25) com Reciprocal Rank Fusion.
  - [ ] Escrever um **eval harness** rodável (golden set de perguntas + métricas automáticas).
- [ ] **Retrofit de guardrails no DentBot ou Seraphina:** PII redaction, prompt injection filtering, budget de contexto, tool allowlist. Documentar como case.
- [ ] **Observability:** adicionar trace IDs + métricas de token/custo/latência em pelo menos 1 projeto (Langfuse ou similar).
- [ ] **Fechar fundamentos Python:** terminar Curso em Vídeo + reescrever 1 projeto antigo com testes (pytest), type hints e Pydantic.

### Renda (curto prazo realista, em USD)
- [ ] Annotation premium: manter pipeline Outlier / Mercor / Alignerr / Mindrift ativo. Atacar a fraqueza conhecida (score inflation, mixing axes) — treinar calibração nos 4 eixos.
- [ ] Freelance AI em USD: usar DentBot como prova social pra prospectar fora do BR (clínicas/SMBs internacionais via Lemon.io, Upwork, contato direto). Alvo: US$ 30–40/hr+.
- [ ] Aplicar a contratos remotos AI/LLM (Lemon.io, Braintrust) — o caminho mais provável de entrada vs. CLT internacional.

### Marca / visibilidade
- [ ] LinkedIn: lançar VishPath com a narrativa (brasileiro, 4 anos Austrália, IA pra imigração). 1 post técnico a cada 2 semanas mostrando os números dos projetos (recall, latência, custo).
- [ ] GitHub: README de cada projeto flagship com arquitetura + métricas + decisões de tradeoff. Pinar os 3 melhores.
- [ ] Portfolio (pablocosta.dev): destacar "production AI, eval-first" como tese, não "júnior buscando primeira oportunidade".

---

## MÉDIO PRAZO — até a formatura (set 2026 → jul 2026 / B.Tech)
**Objetivo:** subir de "junior empregável" para "pleno justificável", fechar profundidade técnica e ter 3 cases com métricas que aguentam entrevista sênior. *Cobre as Fases 6–7 da sequência de estudo.*

### Técnico
- [ ] **Agentic system de verdade:** multi-agente (ex.: Researcher + Analyst + Writer) com tool-calling, memória e MCP. Documentar **failure modes** e como você os mitiga (é o que diferencia pleno de júnior).
- [ ] **Cost optimization como disciplina:** multi-provider routing com failover (OpenAI/Anthropic/Gemini), caching, escolha de modelo por tarefa. Documentar economia em %.
- [ ] **Deploy cloud "de gente grande":** levar 1 projeto além da VPS — AWS/GCP (mesmo free tier), CI/CD, infra as code básico. Vagas mid pedem isso.
- [ ] **Aprofundar avaliação:** estudar frameworks de eval (RAGAS, DeepEval), entender métricas de faithfulness/answer relevancy a fundo. Vira teu diferencial declarado.
- [ ] **Backend FastAPI production-grade:** auth, rate limiting, testes, observability, deploy. Fecha o gap de "eng de software".

### Carreira
- [ ] Montar narrativa de entrevista por **failure mode**: pra cada projeto, saber dizer o que quebrou, como mediu, como consertou. (É a pergunta que separa os níveis.)
- [ ] Pipeline de aplicação dividido em 2 trilhas:
  - **Internacional:** contrato remoto AI/LLM (faixa US$ 65–95/hr mid) → meta de transição pra full-time remoto.
  - **Brasil:** vagas "Python IA Pleno" (agentes, orquestração, observability) — faixa R$ 7–12k, nicho que tá nascendo e onde você já tá à frente.
- [ ] Decidir foco de especialização (profundidade > amplitude): **RAG/retrieval** OU **agentic/orchestration**. O mercado premia depth.

---

## Métricas de sucesso (como saber que funcionou)

| Marco | Curto prazo (3 meses) | Médio prazo (até jul/2026) |
|---|---|---|
| Portfólio | 1 RAG flagship com métricas no README | 3 cases (RAG + agentic + backend) com failure modes documentados |
| Renda USD | Primeiro contrato/freelance em USD fechado | Renda recorrente US$ 2–4k/mês combinada |
| Entrevista | Consegue citar recall@10 dos próprios projetos | Aguenta uma entrevista de AI engineer mid (system design + eval) |
| Marca | LinkedIn ativo, VishPath lançado | Inbound de recrutador/cliente acontecendo |

---

## Princípios que valem o roadmap inteiro
1. **Eval-first.** Todo projeto novo já nasce com métricas. É o que mais te separa do "júnior de chat-with-PDF".
2. **Depth > breadth.** Escolha uma especialização e vá fundo. O mercado paga profundidade.
3. **Mostre número, não tech stack.** "Reduzi custo de inferência em 40%" vence "sei LangChain".
4. **Produção > demo.** Você já tem isso. É teu maior trunfo — explore em toda narrativa.
5. **Não compita na fila errada.** Você não é júnior Python genérico. É AI/LLM application engineer com produção real.

---

## Glossário — termos da sequência de estudo

- **raw API** — chamar o modelo direto pelo SDK/HTTP, montando request e parseando resposta na mão, sem framework. É o que o n8n faz por baixo dos nós visuais.
- **agent loop** — o `while` que você controla: manda mensagem → modelo responde OU pede uma tool → você executa a tool e devolve o resultado → repete até a resposta final. Esse loop *é* o agente; o framework só o esconde.
- **pytest** — framework de teste padrão do Python. Funções `test_*` com `assert` que verificam que o código faz o que promete. Pré-requisito do DeepEval.
- **eval** — medir a qualidade do output de AI com número, repetível (vs. "rodei, olhei, pareceu ok"). Como output de LLM não é determinístico, usa métricas próprias, muitas via LLM-as-judge (faithfulness, recall@k, answer relevancy).
- **DeepEval** — biblioteca que roda eval como pytest. Test cases com métricas em vez de `assert` manual; integra no CI/CD pra barrar prompt ruim antes de subir.

Ordem de aprendizado: **raw API → agent loop** (como o modelo funciona) e **pytest → eval → DeepEval** (como provar que funciona).

---
*Fontes de mercado (jun/2026): vagas e benchmarks salariais (Lemon.io, KORE1, MRJ Recruitment, Built In, Glassdoor BR, Indeed BR, Coursera, NACE/TrueUp); tendência framework→raw API/agent SDK (AI Builder Club, MindStudio, aimultiple); stack de eval (Atlan, Future AGI, Braintrust, genai.qa, DataVLab). Roadmap montado contra requisitos de vagas reais, não survey genérico.*
