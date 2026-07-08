# Roadmap AI/Backend Engineer — Plano de Estudos Completo
**Data:** jun/2026 · **Atualizado:** jul/2026 (correções pesquisadas abaixo) · **Base:** níveis reais auto-avaliados (não o portfólio)
**Projeto-espinha:** Atlas (um AI knowledge assistant que evolui em todas as fases)

> **Nota de atualização (jul/2026):** 3 pontos deste roadmap ficaram desatualizados ou imprecisos entre jun e jul/2026. Correções aplicadas inline, marcadas com `> ⚠️ ATUALIZADO`. Resumo completo no fim do arquivo.

---

## A regra que vale mais que tudo

**Durante o aprendizado, IA é proibida.** Faz na mão → trava → sofre → *depois* confere com IA.

Teu portfólio cheio com retenção zero é a prova do que acontece quando ignora isso. A IA continua sendo tua ferramenta de produção (e tua vantagem real). Mas pra *aprender*, ela sai da frente. Sem exceção nas fases de fundação.

## Como usar este repo (`ai-engineer`) como prova

```
ai-engineer/
├── README.md            ← conta a história: o que é, como evoluiu, o que cada fase prova
├── roadmap.md           ← este arquivo
└── atlas/               ← o projeto-espinha (cresce fase a fase)
    ├── src/
    ├── tests/
    ├── scripts/
    └── README.md        ← arquitetura + decisões
```

**O diferencial não é o código final — é o histórico de commits.** Commita por fase, com mensagens claras. Recrutador abre o `git log` e vê CLI → testado → API → RAG → avaliado → deployado. Essa progressão prova que tu entende cada camada. É o que vibe coder nenhum consegue forjar.

---

## Baseline confirmado por ti

| Área | Nível | Meta |
|---|---|---|
| LLM integration | **3** ✅ | mantém — é tua âncora |
| Python | 1 (fundamentos ok, indo pra POO) | 2 → 3 |
| Docker | 1 (com ajuda de IA) | 3 (solo) |
| Embeddings | 1 (só conceito) | 2 |
| FastAPI | 0 | 2 → 3 |
| pytest | 0 | 2 |
| RAG (do zero) | 0 | 2 |
| LangChain | 0 | 2 |
| LlamaIndex | 0 | 1 |
| AWS | ~0 (curso intro começou) | 1 |

> Horas são estimativas grosseiras. Ajusta pra tua cadência (trabalho + freela + faculdade até jul/2026).

---

# FUNDAÇÃO (idêntica pros dois tracks)

## Fase 0 — Python sólido *(você está aqui)* · ~15–25h
**Objetivo:** Python 1 → 2

**Conteúdos:**
- **Estruturas de dados:** `list`, `dict`, `set`, `tuple` — quando usar cada, mutabilidade, performance
- **Comprehensions:** list/dict/set comprehensions, `generators`, `yield`
- **Controle de fluxo:** loops, `enumerate`, `zip`, unpacking (`*args`, `**kwargs`), `match/case`
- **Funções:** default args, escopo, closures, first-class functions, decorators (básico)
- **OOP (foco da fase):**
  - classes, `__init__`, instance vs class attributes
  - métodos: instance / `@classmethod` / `@staticmethod`
  - herança, composição, polimorfismo, encapsulamento
  - `@property` (getters/setters)
  - dunder methods: `__str__`, `__repr__`, `__eq__`, `__len__`, `__call__`
  - `@dataclass`
  - Abstract Base Classes (`abc.ABC`)
- **Type hints:** `typing` (`Optional`, `Union`/`|`, `Callable`, `Generic`), checagem com `mypy`
- **Async básico:** `async`/`await`, `asyncio.run`, *por que* async pra I/O (chamada de API)
- **Erros & recursos:** `try/except/finally`, exceptions customizadas, context managers (`with`, `__enter__`/`__exit__`)
- **Ambiente:** módulos, packages, imports, `if __name__ == "__main__"`, `venv`, `pip`/`uv`

**Projeto — Atlas v0 (CLI, Python puro):**
- `LLMClient` (classe): wrapper async pra OpenAI/Anthropic, com retry e type hints
- `Message` (dataclass) + `Conversation` (classe): histórico, truncamento por token
- `Assistant` (classe): orquestra `LLMClient` + `Conversation`
- `main.py`: loop de CLI — input → `assistant.ask()` → resposta
- **Entrega:** `python -m atlas` → chat multi-turn funcional no terminal, **tudo digitado por ti**

**Regra da IA:** zero. Lê o traceback tu mesmo.

---

## Fase 1 — Testes desde o dia um · ~10–15h
**Objetivo:** pytest 0 → 2

**Conteúdos:**
- pytest: estrutura, `assert`, convenção de nomes, rodar/filtrar testes
- **Fixtures:** `@pytest.fixture`, `conftest.py`, scopes (function/module/session)
- **Parametrização:** `@pytest.mark.parametrize`
- **Mocking:** `unittest.mock`, `monkeypatch`, mockar chamada de API/LLM (não gastar token em teste)
- **Async:** `pytest-asyncio` pra testar `LLMClient`
- **Coverage:** `pytest-cov`
- Padrão Arrange-Act-Assert; testar happy path + edge cases + erros

**Projeto — Atlas v1 (testado):**
- Mockar `LLMClient` (sem chamar API real)
- Testar lógica de truncamento do `Conversation`, retry, tratamento de erro
- **Entrega:** `pytest` verde, coverage > 80% no core

**Regra da IA:** escreve os testes na mão. Eles são o que prova que tu entende teu próprio código.

---

## Fase 2 — FastAPI na mão · ~20–30h
**Objetivo:** FastAPI 0 → 2

**Conteúdos:**
- ASGI vs WSGI, `uvicorn`
- Rotas, path/query params, request body
- **Pydantic v2:** `BaseModel`, validators, `Field`, `response_model`, `pydantic-settings`
- Endpoints async
- **Dependency Injection:** `Depends`
- Middleware, CORS, exception handlers customizados
- Status codes, `HTTPException`
- **Streaming:** `StreamingResponse` / SSE (pra token streaming do LLM)
- `BackgroundTasks`
- Auth básico (API key / bearer token)
- Docs automáticas (OpenAPI/Swagger)
- Testar com `TestClient` / `httpx`

**Projeto — Atlas v2 (API):**
- `POST /chat` com request/response Pydantic + streaming
- `Assistant` injetado via `Depends`, auth por API key, exception handler, CORS
- Testes de endpoint com `TestClient`
- **Entrega:** `uvicorn` rodando, Swagger funcional, suíte verde

**Regra da IA:** reconstrói linha por linha algo que tu antes fez com IA. Sente a diferença.

---

## Fase 3 — RAG do primeiro princípio · ~25–35h *(a fase mais importante)*
**Objetivo:** RAG 0 → 2, pgvector 0 → 2, embeddings 1 → 2, LangChain 0 → 2

**Conteúdos:**
- **Embeddings:** o que é, dimensionalidade, modelos (`text-embedding-3-small`), custo
- **Similaridade:** cosine vs dot product vs L2 — diferença e quando usar cada
- **Chunking:** fixed-size, por sentença, recursive, `overlap` — trade-offs
- **Vector store na mão:** numpy, busca linear top-k (entender o que o framework esconde)
- **pgvector (cobre dois 0s de uma vez):**
  - extensão, tipo `vector(n)`
  - operadores: `<=>` (cosine), `<->` (L2), `<#>` (inner product)
  - índices: IVFFlat vs HNSW
    > ⚠️ **ATUALIZADO:** não é mais um trade-off neutro. HNSW é o default de 2026 — maior recall, menor latência, e pode ser criado com a tabela ainda vazia (importante pra CI/CD e blue/green deploy). IVFFlat só se justifica em cenário bem específico: ingestão acima de ~100k writes/hora, e mesmo aí HNSW costuma competir bem. Trata HNSW como escolha padrão e documenta IVFFlat como exceção, não como alternativa de peso igual.
  - retrieval com SQL puro
- **Pipeline RAG completo:** ingest → chunk → embed → store → retrieve → augment prompt → generate
- **Qualidade:** tuning de top-k, metadata filtering, reranking (conceito)
- **LangChain v1.x:** document loaders, text splitters, vector store integration, retrievers
  > ⚠️ **ATUALIZADO:** LangChain 1.0 (release estável, out/2025) deprecou o padrão LCEL (`prompt | llm | parser`) em favor de `create_agent` + sistema de middleware (human-in-the-loop, summarization, PII redaction). Quem estuda LCEL agora aprende algo que o próprio LangChain está abandonando. Estuda `create_agent`, middleware, e tool calling nativo — não LCEL.
- **LlamaIndex:** tour rápido (index + query engine) — só pra saber a diferença (nível 1)

**Projeto — Atlas v3 (com conhecimento). Ordem obrigatória:**
1. **Na mão:** `/ingest` que chunka + embeda + guarda em store numpy in-memory; retrieval por cosine top-k
2. **pgvector:** trocar o store in-memory por tabela Postgres com pgvector
3. **LangChain (opcional):** refatorar o retrieval com retriever do framework — agora tu *vê* o que ele abstrai
4. `/chat` passa a fazer retrieval + augment + generate
- **Entrega:** Atlas responde perguntas sobre **teus próprios docs** (tuas notas de estudo, ou docs de um cliente)

**Regra da IA:** NÃO começa pelo framework. Mão → pgvector → framework. Entrevista abre o capô.

---

## Fase 4 — Evals & observability · ~12–18h
**Objetivo:** evals 0 → 2 (teu atalho — músculo do Outlier transfere)

**Conteúdos:**
- *Por que* avaliar LLM: não-determinismo, regressão silenciosa
- **Langfuse:** tracing, spans, custo, latência; self-host (na tua VPS, joga a favor do teu Docker)
  > ⚠️ **ATUALIZADO:** confirmado que Langfuse continua ativo e é padrão de mercado (usado por Canva, integra nativamente com LangChain/LlamaIndex/OTel) — mas desde a v3 o self-host virou stack de 6 containers (Postgres + ClickHouse + Redis + MinIO + web + worker), não só Postgres como antes. Recomendação oficial: mínimo 4GB RAM, 8GB confortável. Antes de comprometer a VPS, decide: v3 completo (production-grade, mais pesado) ou v2 (só Postgres, mais simples, ainda suportado mas não é mais pra onde o projeto está indo). Pro Atlas, v2 provavelmente basta e evita competir por RAM com o resto do teu stack (n8n, Evolution API, Chatwoot já rodando na mesma VPS).
- **Métricas de RAG:** faithfulness, answer relevancy, context precision/recall
- **ragas:** setup, montar golden test set, rodar avaliação
  > ✅ **CONFIRMADO:** ragas segue ativo e é referência de mercado pra métricas de RAG (faithfulness, context precision/recall). Ponto real: é só biblioteca de métricas, sem dashboard/observability própria — por isso a combinação com Langfuse no roadmap (eval offline com ragas + tracing em produção com Langfuse) é a arquitetura certa, não redundância.
- LLM-as-judge (conceito + armadilhas)
- Conexão com rubrica multi-eixo (Outlier: instruction following, consistency, quality)

**Projeto — Atlas v4 (observável e avaliado):**
- Langfuse instrumentando `LLMClient` + retrieval
- `scripts/eval.py`: test set + ragas (faithfulness, context precision)
- **Entrega:** dashboard Langfuse + relatório de eval versionado no repo (mede uma melhoria que tu fez)

**Regra da IA:** medir output > "olhar e achar bonito". É o diferenciador citado nos take-homes da OpenAI.

---

## Fase 5 — Docker solo + AWS base · ~15–20h
**Objetivo:** Docker 1 → 3 (solo), AWS 0 → 1

**Conteúdos:**
- **Dockerfile:** layers, multi-stage build, `.dockerignore`, usuário non-root, `HEALTHCHECK`
- **docker-compose:** multi-serviço (app + postgres/pgvector), volumes, networks, env
- Otimização de tamanho de imagem
- **AWS:** IAM (users/roles/policies), S3 (`boto3`), EC2 (básico), conceito de VPC
  > ✅ **CONFIRMADO:** IAM/EC2/S3/VPC seguem sendo a base universal pedida em 2026, com ou sem IA — sem mudança aqui.
  > 💡 **OPCIONAL (decide tu):** vagas que combinam AWS + IA citam cada vez mais **Bedrock** (API gerenciada da AWS pra servir LLMs, tipo Claude/Llama via boto3) — não é treino, é só mais uma forma de *aplicar* LLM em produção, o que já é teu princípio. Não é essencial pra fundação; só relevante se mirar vaga que pede especificamente AWS+IA, ou se quiser um segundo caminho de servir LLM além de chamar OpenAI/Anthropic direto.
- PaaS vs IaaS — *por que* Railway/Render ≠ cloud primitives
- Secrets (env vars, conceito de Secrets Manager)

**Projeto — Atlas v5 (deployado):**
- Dockerfile multi-stage + compose (atlas + postgres/pgvector + healthcheck)
- Deploy (VPS ou cloud) + S3 pra armazenar docs ingeridos
- **Entrega:** Atlas no ar com URL pública + README com diagrama de arquitetura

**Regra da IA:** escreve o Dockerfile e o compose do zero. Sai da muleta.

---

# A BIFURCAÇÃO (decide depois da Fundação)

A fundação acima serve aos dois. A diferença é o que tu adiciona no fim.

## → Track EMPREGO (remoto internacional, USD)
**Conteúdos extras:**
- **LLM system design:** desenhar RAG/agent em produção no quadro — caching, fallback, rate limit, eval gate, multi-tenancy
- **DSA prático:** ~30–40 Easy/Medium (NeetCode 150 lite). Padrões: hashmap, two pointers, sliding window, BFS/DFS. Não vira competitive programmer — só não trava.
  > ✅ **CONFIRMADO:** pesquisa de vagas 2026 mostra que DSA pesado (LeetCode medium/hard, rodadas dedicadas) é padrão só em FAANG-tier. Pra empresas mid-size e a maioria das remotas internacionais, o esperado é cobrir ~12-15 padrões centrais com confiança — exatamente a calibração que já está aqui. Sem mudança.
- **Take-home polish:** entregar projeto completo + README + decision log + testes em 48h. Pequeno e completo > ambicioso e quebrado.
- **Posicionamento:** mid AI/backend com fundamentos defensáveis (agora tu sustenta o portfólio).

## → Track BUILDER (freela/agência/SaaS)
**Conteúdos extras:**
- Deployment profundo: CI/CD (GitHub Actions), monitoring, multi-tenant, billing real (fechar VishPath/readinghands)
- Produtizar a orquestração: Atlas/DentBot viram template replicável
- **Posicionamento:** AI automation specialist que entrega rápido. Mercado não proíbe IA — premia velocidade.
- **Vantagem:** tu já fatura nisso. Risco menor, retorno mais rápido.

---

## O que NÃO está na fundação (de propósito)
- **Pinecone/Qdrant/Weaviate:** pula. pgvector cobre 90% dos casos e tu já roda Postgres. Aprende os gerenciados só se uma vaga pedir.
- **Fine-tuning / treino de modelo:** não é teu caminho. Foco é *aplicar* LLM, não treinar.

---

## Resumo das correções (pesquisa jul/2026)

| # | Seção | Estava | Correção | Fonte |
|---|---|---|---|---|
| 1 | Fase 3 — LangChain | "LCEL básico" | LangChain 1.0 (out/2025) deprecou LCEL → usa `create_agent` + middleware | langchain.com/blog, changelog.langchain.com |
| 2 | Fase 3 — pgvector | IVFFlat vs HNSW como trade-off neutro | HNSW é o default 2026; IVFFlat só acima de ~100k writes/hora | dbi-services.com, danubedata.ro (mar/2026) |
| 3 | Fase 4 — Langfuse | "self-host, joga a favor do teu Docker" (implicava simples) | v3 = stack de 6 containers (Postgres+ClickHouse+Redis+MinIO+web+worker), mín. 4GB RAM. v2 (só Postgres) ainda existe e é mais leve — decide antes de comprometer a VPS | langfuse.com/self-hosting, jangwook.net (mai/2026) |
| — | Fase 4 — ragas | (sem verificação) | Confirmado ativo e é a referência de mercado; combinação com Langfuse é arquitetura certa (métricas offline + tracing em produção), não redundância | futureagi.substack.com, braintrust.dev |
| — | Fase 5 — AWS | (sem verificação) | Confirmado: IAM/EC2/S3/VPC seguem base correta pra 2026. Adição opcional: Bedrock aparece em vagas que combinam AWS+IA — não essencial, decisão tua | dev.to (mar/2026), interviewkickstart.com, scaler.com |
| — | Track Emprego — DSA/NeetCode | (sem verificação) | Confirmado: DSA pesado é só padrão FAANG-tier. Mid-size/remoto internacional pede ~12-15 padrões centrais — calibração do roadmap (30-40 Easy/Medium) já está certa | medium.com/@codegrey (jun/2026), namastedev.com |

**Todos os blocos do roadmap agora foram pesquisados e validados ou corrigidos.**

**Resto do documento:** validado contra vagas reais de "AI/Backend Engineer" remoto (FastAPI + Postgres + Docker + auth + RAG aparecem repetidamente) — estrutura de fases, ordem (mão → pgvector → framework), regra "sem IA no aprendizado" e uso do git log como prova seguem corretos, sem necessidade de mudança.