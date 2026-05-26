# AI Engineer Study Map

> Owner: Pablo Costa
> Estimativa: ~210h total (~14 semanas a 15h/semana)
> Pressuposto: já dominas Java/Spring, Postgres básico, Docker, Git, Python intermediário

## Como usar este mapa

- **Sequencial.** Cada fase depende da anterior. Não pula.
- **70% mãos na massa, 30% teoria.** Cada bloco tem um "check de domínio" — um build pequeno que prova que entendeste, não só viu vídeo.
- **Recursos curados, não exaustivos.** Listei 2-3 por bloco. Se quiser mais, é porque está procrastinando.
- **Anti tutorial hell:** se está há 3 dias num bloco sem produzir nada, pula pro check de domínio e força.

## Mentalidade: AI Engineer vs ML Engineer

**AI Engineer** = constrói aplicações com LLMs como tijolo. Não treina modelo. Usa API, faz RAG, agentes, eval, deploy. **É o teu target.**

**ML Engineer** = treina/fine-tuna modelos, pipelines de dados, MLOps. Exige matemática, PyTorch, anos. **Não é o teu target.**

Esse mapa é AI Engineer puro. Zero PyTorch, zero fine-tuning, zero math pesado.

---

## Fase 1 — Python sólido + Backend (Weeks 1-3, ~45h)

### 1.1 Python avançado (~15h)

**Por quê:** "Python intermediário" não passa em entrevista entry-level de AI Engineer. Type hints rigoroso, async, pytest, e logging estruturado são esperados como padrão.

**Frame:** "avançado" aqui ≠ CPython core dev. Mira em **"código que passa em code review de um mid-level sênior"**, não em domínio do GIL ou metaclasses. Organizado por consequência: must-have = não passa sem; should-have = esperado em produção; nice-to-have = diferencia.

---

#### Must-have (sem isso não passa)

**M1. Type hints completos e modernos**

Toda função tipada. Sem `Any` por preguiça. Sintaxe Python 3.10+.

```python
# ❌ Intermediário
def search(query, top_k=5):
    return [...]

# ✅ Entry-level pronto
def search(query: str, top_k: int = 5) -> list[Document]:
    return [...]
```

Domina: `list[X]`, `dict[K, V]`, `X | None` (em vez de `Optional[X]`), `Callable[[int], str]`, `TypedDict`, `Protocol` pra duck typing tipado, `Literal["a", "b"]`. Roda `mypy` ou `pyright` no projeto.

**M2. Pydantic v2**

Sem isso, AI Engineer não existe. Schemas de I/O de LLM, config, validação.

```python
from pydantic import BaseModel, Field

class SearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=500)
    top_k: int = Field(default=5, ge=1, le=100)
    filters: dict[str, str] | None = None
```

Domina: `BaseModel`, field validators (`@field_validator`), `model_dump()`, `model_validate()`, `model_validate_json()`, `Settings` com `pydantic-settings` pra env vars.

**M3. Async/await aplicado**

Saber **quando** usar: I/O bound (chamadas LLM, HTTP, DB). Não pra CPU.

```python
import asyncio
import httpx

async def fetch_all(urls: list[str]) -> list[dict]:
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return [r.json() for r in responses]
```

Domina: `async def`, `await`, `asyncio.gather` (paralelismo), `asyncio.create_task`, async context managers (`async with`), `httpx` async client. Sabe explicar por que async não acelera CPU-bound code.

**M4. Error handling profissional**

Sem `except Exception: pass`. Sem `except:` pelado. Custom exceptions onde fizer sentido.

```python
class RetrievalError(Exception):
    """Raised when document retrieval fails."""

class EmbeddingError(RetrievalError):
    """Raised when embedding generation fails."""

try:
    embedding = await get_embedding(text)
except httpx.HTTPStatusError as e:
    raise EmbeddingError(f"Embedding API returned {e.response.status_code}") from e
```

Domina: `try/except` específico por tipo, `raise X from e` (exception chaining), custom exception hierarchies, `finally` pra cleanup. Sabe a diferença entre `raise` e `raise from`.

**M5. Pytest sólido**

```python
import pytest

@pytest.fixture
def sample_docs() -> list[str]:
    return ["doc1", "doc2", "doc3"]

@pytest.mark.parametrize("query,expected_count", [
    ("python", 2),
    ("nonexistent", 0),
])
def test_search_returns_expected_count(query, expected_count, sample_docs):
    results = search(query, sample_docs)
    assert len(results) == expected_count

@pytest.mark.asyncio
async def test_async_search():
    result = await async_search("query")
    assert result is not None
```

Domina: fixtures, `@pytest.mark.parametrize`, `pytest-asyncio` pra async, mocking com `unittest.mock` ou `pytest-mock`, organização `tests/` directory.

**M6. Estrutura de projeto moderna**

Já dominas Java/Maven — analogia direta. Em Python 2026:

- **`uv`** (não `pip` puro, não `poetry` mais) — gerenciador de deps moderno, super rápido
- **`pyproject.toml`** — único arquivo de config (substitui `setup.py`, `requirements.txt`, `setup.cfg`)
- **Ruff** — linter + formatter (substitui black + flake8 + isort + pylint, tudo num só)
- **mypy** ou **pyright** — type checker
- Layout `src/your_package/` (não package no root)

```bash
uv init my-rag-app
uv add fastapi pydantic openai
uv add --dev pytest ruff mypy
uv run pytest
uv run ruff check .
uv run mypy src/
```

Sabe explicar a diferença entre runtime deps e dev deps, e por que `requirements.txt` puro não é o suficiente em 2026.

---

#### Should-have (esperado em código de produção)

**S1. Logging estruturado (não print)**

```python
import logging
logger = logging.getLogger(__name__)

# ❌
print(f"Got {len(results)} results")

# ✅
logger.info("retrieval_completed", extra={"result_count": len(results), "query": query})
```

Bonus moderno: `structlog` (logs como JSON estruturado, fácil de parsear).

**S2. `pathlib` em vez de `os.path`**

```python
# ❌
import os
file_path = os.path.join("data", "docs", "file.txt")

# ✅
from pathlib import Path
file_path = Path("data") / "docs" / "file.txt"
```

Domina: `Path.read_text()`, `Path.write_text()`, `Path.glob()`, `Path.iterdir()`.

**S3. Dataclasses ou Pydantic (não dicts soltos)**

```python
# ❌
result = {"text": "...", "score": 0.92, "metadata": {...}}

# ✅
from dataclasses import dataclass

@dataclass
class SearchResult:
    text: str
    score: float
    metadata: dict[str, str]
```

Quando usar `@dataclass` vs Pydantic: dataclass pra estruturas internas; Pydantic pra anything I/O (API, DB, config).

**S4. Context managers**

Usar `with` corretamente, e saber criar custom:

```python
from contextlib import contextmanager

@contextmanager
def timed_operation(name: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        logger.info("operation_completed", extra={"name": name, "elapsed_s": elapsed})

with timed_operation("retrieval"):
    results = retrieve(query)
```

**S5. Generators e comprehensions**

```python
# Comprehensions sólidas
embeddings = [embed(doc) for doc in docs if len(doc) > 0]

# Generators pra streaming/lazy eval
def chunk_iterator(docs: list[str], size: int = 100) -> Iterator[list[str]]:
    for i in range(0, len(docs), size):
        yield docs[i:i + size]
```

Sabe quando comprehension fica ilegível e deve virar loop. Sabe usar `yield` pra processar coisas grandes sem carregar tudo em memória.

**S6. `functools` essencial**

```python
from functools import lru_cache, wraps, partial

@lru_cache(maxsize=128)
def get_embedding_cached(text: str) -> list[float]:
    return get_embedding(text)
```

Domina: `lru_cache`, `wraps` (em decorators custom), `partial`.

---

#### Nice-to-have (diferencia)

**N1. Decorators custom úteis**

```python
def retry(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts - 1:
                        raise
                    await asyncio.sleep(delay * (2 ** attempt))
        return wrapper
    return decorator
```

**N2. `itertools` quando cabe**

`chain`, `groupby`, `islice`, `batched` (3.12+). Não força — só quando a solução com `itertools` fica mais clara que loop.

**N3. CLI moderna com `typer`**

Mesmo autor do FastAPI. Mais ergonômico que `argparse`:

```python
import typer

app = typer.Typer()

@app.command()
def ingest(source: Path, batch_size: int = 100):
    """Ingest documents from source into vector store."""
    ...
```

---

#### O que ESQUECER (red flags inversas)

Não estuda esses até estar mid-level pleno. Se um curso "Python Avançado" gasta 3 aulas com isso, pula o curso.

- **Metaclasses** — 99% dos AI Engineers nunca usam
- **Descriptors** — abstração pesada, irrelevante
- **`__slots__`** — otimização que raramente importa
- **asyncio internals** (event loops, transports) — saber usar `asyncio.gather` basta
- **GIL profundo** — saiba que existe, não filosofa
- **Threading complexo** — async + multiprocessing cobre 99% dos casos AI
- **C extensions / Cython / Numba** — não é teu mundo
- **Type system avançado** (variance, `TypeVar` com bounds complexos)

---

#### Self-assessment (10 perguntas)

Responde sinceramente. Se não consegues, ainda tem gap:

1. Sabes escrever uma função async que faz 10 chamadas HTTP em paralelo e retorna resultados ordenados? (`asyncio.gather`)
2. Sabes a diferença entre `list[X]` e `tuple[X, ...]` no type hint e quando usar cada?
3. Sabes criar um `BaseModel` Pydantic com validator custom que rejeita strings vazias?
4. Sabes escrever um teste pytest com fixture + parametrize?
5. Sabes a diferença entre `raise e` e `raise NewError() from e`?
6. Sabes por que `@dataclass(frozen=True)` é útil?
7. Sabes setupar um projeto novo com `uv init`, adicionar deps, e rodar `ruff check`?
8. Sabes explicar quando usar `@property` em vez de um método?
9. Consegues ler uma stack trace de exception chained e identificar causa raiz?
10. Sabes a diferença entre `Path("a") / "b"` e `os.path.join("a", "b")` além da sintaxe?

**8+ "sim":** entry-level Python solid. Vai pra Fase 1.2.
**5-7 "sim":** ainda tem 1-2 semanas de gap. Foca nos blocos M.
**<5 "sim":** investe 2-3 semanas aqui antes de continuar.

---

**Recursos:**
- **Fluent Python, 2ª ed** (Luciano Ramalho) — capítulos 5, 8, 9, 17, 19, 21. Esse é o livro.
- **Pydantic v2 docs** — primeiros 4 capítulos
- **uv docs** (astral.sh/uv) — quickstart é curto e essencial
- **Ruff docs** — configuration

**Roteiro prático de 2 semanas (~30h):**

*Semana 1 (~15h):*
- Fluent Python capítulos 5 (dataclasses), 8 (type hints), 9 (decorators e closures), 19 (concorrência)
- Setup projeto novo do zero com `uv` + ruff + mypy + pytest. Configura tudo.

*Semana 2 (~15h):*
- Fluent Python capítulos 17 (iterators/generators) e 21 (asyncio)
- Refactor de 1 projeto teu (DentBot ou Pioneira) aplicando: 100% type hints, ruff sem warnings, mypy sem errors, pytest cobrindo fluxo principal, structured logging substituindo prints.

**Check de domínio:** o refactor da semana 2 é o check. Se consegues fazer isso e o código fica legível, está pronto pra Fase 1.2. Bonus: roda `mypy --strict` e zero erros.

---

### 1.2 FastAPI + Async (~20h)

**Por quê:** padrão de fato em vagas AI Engineer. Streaming SSE é table stakes pra LLM apps.

**Conteúdo:**
- Routers, dependency injection
- Pydantic models como schemas
- Async endpoints + concurrent requests
- **Streaming responses (SSE)** — crítico pra LLMs
- Middleware (CORS, auth, logging)
- Background tasks
- Auth com JWT (mesmo que básica)
- Testing com `TestClient` e `httpx`

**Recursos:**
- **FastAPI docs oficiais** — são tutoriais. Faz do início ao fim. Não pula.
- **"FastAPI for Busy Engineers"** ou similar — vídeo
- Sebastián Ramírez no YouTube

**Check de domínio:** API com auth JWT, 1 endpoint que faz streaming de uma chamada OpenAI, deployed local via docker-compose com Postgres.

---

### 1.3 Postgres avançado para AI (~10h)

**Por quê:** vai usar pgvector. Sem entender índices e EXPLAIN, otimização é chute.

**Conteúdo:**
- Indexes (B-tree, GIN, GiST, HNSW)
- `EXPLAIN ANALYZE` lendo planos de query
- JSONB (queries, indexação)
- Full-text search com `tsvector`/`tsquery` (vai usar pra BM25)
- Transactions, isolation levels (básico)

**Recursos:**
- **"Postgres for the Modern Web"** ou docs oficiais
- **pgvector README** (vai aprofundar na Fase 3)

**Check de domínio:** schema com JSONB + full-text search funcionando, EXPLAIN mostrando uso de índice.

---

## Fase 2 — LLM APIs fundamentais (Weeks 4-5, ~30h)

> Regra dura: **nenhum framework nesta fase.** SDK puro. Entender primitivos antes de abstrair.

### 2.1 OpenAI SDK direto (~10h)

**Conteúdo:**
- Chat completions API
- Streaming
- **Tool/function calling** (essencial)
- Structured outputs (JSON mode + response schemas)
- Embeddings API (`text-embedding-3-small/large`)
- Vision (multi-modal)
- Token counting (`tiktoken`)

**Recursos:**
- **OpenAI Cookbook** no GitHub — `github.com/openai/openai-cookbook`. Vai direto nos exemplos práticos.
- **OpenAI API docs** — reference

**Check de domínio:** CLI chatbot em Python com (a) streaming, (b) tool calling pra um cálculo simples, (c) JSON mode estruturado.

---

### 2.2 Anthropic SDK (~8h)

**Por quê:** dois providers = fallback + cost optimization + diferentes strengths (Claude é melhor pra long context, OpenAI tem ecosystem maior).

**Conteúdo:**
- Messages API
- System prompts (Anthropic separa system explicitamente)
- Tool use (sintaxe diferente do OpenAI)
- Vision
- **Prompt caching** (economia de até 90% em prompts longos)

**Recursos:**
- **Anthropic Cookbook** — `github.com/anthropics/anthropic-cookbook`
- **Anthropic docs** — leitura completa do "Build with Claude"

**Check de domínio:** refactora o CLI chatbot pra alternar entre OpenAI e Anthropic via env var, mesma interface.

---

### 2.3 Prompt Engineering aplicado (~12h)

**Por quê:** skill explícita em job postings, e é o que separa boa app de app medíocre.

**Conteúdo:**
- System vs user prompts (e quando usar cada)
- Few-shot examples
- Chain-of-thought (e quando ajuda vs quando atrapalha)
- Structured outputs (XML tags do Anthropic, JSON do OpenAI)
- Prompt templates e composability
- Prompt injection (defesa)
- Avaliação manual de prompts

**Recursos:**
- **Anthropic's "Prompt Engineering Interactive Tutorial"** (Jupyter notebooks no GitHub). É o melhor recurso free.
- **OpenAI's "GPT best practices"** guide
- **Lilian Weng's "Prompt Engineering"** post (lilianweng.github.io)

**Check de domínio:** documenta uma biblioteca de 5-10 prompts patterns que tu uses, cada um com (a) intent, (b) template, (c) exemplo de I/O, (d) anti-pattern que estava antes.

---

## Fase 3 — RAG (Weeks 6-8, ~45h)

> O tópico mais pedido em vagas AI Engineer. É onde está a maioria do trabalho real.

### 3.1 Embeddings fundamentos (~5h)

**Conteúdo:**
- O que são embeddings (vetor denso representando semântica)
- Cosine similarity vs dot product vs euclidean
- Modelos: OpenAI (`text-embedding-3-*`), Voyage AI, Cohere, BGE (open source)
- Dimensionality e truncation
- Custo e velocidade (batch APIs)

**Recursos:**
- **Cohere LLM University** — módulos de embeddings (free, excelente)
- **Sebastian Raschka** posts sobre embeddings

**Check de domínio:** explicar em 3 minutos pra um não-técnico o que é embedding e por que `Rei - Homem + Mulher ≈ Rainha`.

---

### 3.2 Vector databases (~10h)

**Conteúdo:**
- **pgvector primeiro** (já dominas Postgres — single source of truth)
- Pinecone (padrão SaaS US)
- FAISS (in-memory, bom pra prototyping)
- Índices: HNSW (default moderno), IVF, flat
- Trade-offs: recall vs latency vs cost

**Recursos:**
- **pgvector README** (no GitHub) — completo, curto
- **Pinecone Learning Center** — `pinecone.io/learn` (gratuito, muito bom)

**Check de domínio:** mesmo dataset (uns 1000 docs) indexado em pgvector E Pinecone, comparar latência e qualidade.

---

### 3.3 RAG básico (~5h)

**Conteúdo:**
- Pipeline: ingestion → chunking → embedding → indexing → retrieval → generation
- Chunking estratégias: fixed-size, recursive, semantic
- Top-K retrieval
- Context window management
- Citation tracking

**Recursos:**
- **LangChain RAG tutorial** (mas usa SDK puro primeiro, depois LangChain na Fase 4)
- **"RAG from Scratch"** série do LangChain no YouTube — Lance Martin

**Check de domínio:** chat-with-PDF funcional sem framework (só OpenAI + pgvector).

---

### 3.4 RAG avançado (production-grade) (~15h)

**Por quê:** chat-with-PDF é trivial. O que paga é o RAG que funciona com 1M docs.

**Conteúdo:**
- **Hybrid search**: vector (dense) + BM25 (sparse, via Postgres FTS)
- **RRF** (Reciprocal Rank Fusion) pra fundir rankings
- **Reranking** com Cross-Encoders (Cohere Rerank API, BGE reranker)
- **Query transformation**: rewrite, decomposition, HyDE
- **Contextual Retrieval** (Anthropic's technique)
- Parent-child chunking, sliding window
- Metadata filtering

**Recursos:**
- **Anthropic's "Contextual Retrieval"** blog post (anthropic.com/news/contextual-retrieval) — leitura obrigatória
- **Wenqi Glantz** "Advanced RAG" series no Medium
- **Pinecone advanced RAG guides** no Learning Center
- **"Building and Evaluating Advanced RAG"** — DeepLearning.AI short course (free, 1h)

**Check de domínio:** sistema RAG com hybrid search + reranking, comparado contra RAG vanilla em métricas.

---

### 3.5 Eval de RAG (~10h)

**Por quê:** "It works" sem métrica = desqualificação em entrevista.

**Conteúdo:**
- Métricas: groundedness, answer relevance, context precision/recall
- Hit rate, MRR (Mean Reciprocal Rank)
- LLM-as-judge para scoring
- Eval datasets (criar manualmente + sintético)
- Regression testing

**Recursos:**
- **Hamel Husain — "Your AI Product Needs Evals"** (hamel.dev). O post definitivo. Lê 2x.
- **Ragas** library docs (`docs.ragas.io`)
- **Eugene Yan** posts sobre eval (eugeneyan.com)

**Check de domínio:** eval set de 30+ queries do teu RAG, scoring automatizado, regression test que falha CI se métrica cai.

---

## Fase 4 — Orquestração (Weeks 9-10, ~30h)

### 4.1 LangChain LCEL (~15h)

**Por quê:** framework #1 em job listings (34.3% das vagas agentic). Mas use com cabeça — entender primitivos primeiro (Fase 2) torna LangChain transparente.

**Conteúdo:**
- Runnables e composability
- LCEL (LangChain Expression Language)
- Chains (RAG chain, conversational chain)
- Tools e tool binding
- Output parsers
- Memory abstractions
- Callbacks e streaming

**Recursos:**
- **LangChain docs** — quickstart + LCEL section
- **DeepLearning.AI** — "LangChain for LLM Application Development" (Harrison Chase, free, ~1h30)

**Check de domínio:** mesmo chatbot da Fase 2, mas implementado com LCEL — comparar legibilidade e flexibilidade.

---

### 4.2 LangGraph (~15h)

**Por quê:** agentic systems é onde está o premium ($150K+ em listings senior). LangGraph é o padrão pra workflows com state.

**Conteúdo:**
- State graphs (nodes, edges, conditional edges)
- Persistent state
- Multi-step reasoning (plan → execute → reflect)
- Human-in-the-loop
- Multi-agent patterns (supervisor, swarm)
- Streaming intermediate steps

**Recursos:**
- **LangGraph docs** — tutorials section
- **DeepLearning.AI** — "AI Agents in LangGraph" (free)
- **LangGraph examples repo** no GitHub

**Check de domínio:** research agent com loop plan-search-synthesize-critique-refine, state visualizado.

---

## Fase 5 — MCP (Week 11, ~15h)

**Por quê:** **o item mais alto-leverage do mapa todo.** Padrão emergente (~97M downloads/mês em Fev/2026), suportado por Anthropic/OpenAI/Google/Microsoft. Quase ninguém tem MCP server público — diferencial bruto.

**Conteúdo:**
- Spec do protocolo (transport, messages, lifecycle)
- Tools, Resources, Prompts (os 3 conceitos centrais)
- Server SDK (Python — FastMCP)
- Client integration
- Publishing (npm/PyPI)

**Recursos:**
- **modelcontextprotocol.io** — site oficial, specs e exemplos
- **Anthropic's MCP introduction blog**
- **FastMCP no GitHub** — Python SDK que tu já mexeu (Mercor)
- **MCP servers awesome list** — referência de exemplos

**Check de domínio:** publica 1 MCP server teu no GitHub (e PyPI se aplicável). Recomendação: `devdocs-mcp` que faz Q&A sobre documentação técnica — usa teu RAG da Fase 3.

---

## Fase 6 — Eval + Observability (Week 12, ~15h)

### 6.1 LangSmith (~8h)

**Conteúdo:**
- Tracing (cada chamada LLM visível)
- Datasets (criar, versionar)
- Evaluators (LLM-as-judge, custom Python)
- Regression testing automatizado

**Recursos:**
- **LangSmith docs** — quickstart + evaluators
- **DeepLearning.AI** — curso de LLMOps tem cobertura

**Check de domínio:** instrumentar tua app RAG com tracing, eval dataset, e dashboard.

---

### 6.2 Alternativas de observability (~3h, leitura)

**Conteúdo:**
- Phoenix (Arize) — open source, similar
- Helicone — proxy-based, simples
- Quando escolher cada

**Recurso:** posts comparativos. Não precisa dominar — só conhecer pra entrevista.

---

### 6.3 LLM-as-judge avançado (~4h)

**Conteúdo:**
- Prompts de eval (rubrics)
- Pairwise vs absolute scoring
- Calibração (agreement com humano)
- Anti-patterns (judge bias)

**Recursos:**
- **Eugene Yan** — "Patterns for Building LLM-based Systems & Products"
- **Hamel Husain** — outros posts no hamel.dev

---

## Fase 7 — Cloud + Deploy (Weeks 13-14, ~30h)

### 7.1 Docker refinement (~3h)

Já dominas básico. Foco:
- Multi-stage builds
- Otimização de layers
- docker-compose pra dev stack (Postgres + pgvector + Redis + app)

---

### 7.2 AWS para AI (~15h)

**Por quê:** AWS aparece em 32.9% das vagas AI. Não vire AWS expert — mira no essencial.

**Conteúdo:**
- Lambda + API Gateway (deploy de FastAPI app)
- S3 (storage de docs, eval datasets)
- IAM básico
- CloudWatch logs
- **Bedrock basics** (acesso a Claude/outros via AWS)
- Secrets Manager

**Recursos:**
- **AWS docs** + **"Serverless Land"** templates
- **"AWS for Python Devs"** — ou cursos curtos focados

**Check de domínio:** deploy de FastAPI no Lambda via Mangum, com Secrets Manager pra API keys.

---

### 7.3 Alternativa moderna: Modal (~5h)

**Por quê:** Python-first, AI-focused, sem AWS pain. Listings de AI startup citam frequentemente.

**Recurso:** **modal.com/docs** — quickstart é excelente

**Check de domínio:** deploy do research agent (Fase 4) no Modal.

---

### 7.4 Railway / Fly.io (~3h)

Para projetos pessoais e MVPs. Setup trivial. Vale ter no portfolio.

---

### 7.5 GitHub Actions (~4h)

CI/CD básico:
- Run tests em PR
- Deploy automático em merge
- Eval regression como gate

---

## Referência permanente (assinar / seguir)

**Blogs (leitura obrigatória recorrente):**
- **Hamel Husain** — hamel.dev (eval, MLOps aplicado)
- **Eugene Yan** — eugeneyan.com (LLM systems patterns)
- **Simon Willison** — simonwillison.net (newsletter diária, LLM tools)
- **Chip Huyen** — huyenchip.com (designing AI systems)
- **Lilian Weng** — lilianweng.github.io (deep dives técnicos)
- **Anthropic Engineering blog** — anthropic.com/news (Contextual Retrieval, Computer Use, MCP)

**Podcasts:**
- **Latent Space** (Swyx) — semanal, AI Engineering puro
- **The Cognitive Revolution** — entrevistas profundas

**Newsletters:**
- **AI Engineer** (newsletter do Swyx) — gratuita
- **The Pragmatic Engineer** (paga, vale)

**YouTube:**
- **Andrew Ng / DeepLearning.AI** — todos os short courses (1-2h cada, gratuitos)
- **LangChain** channel — overviews

---

## Livros (3 essenciais, não mais)

1. **"AI Engineering"** — Chip Huyen (2024/2025). O livro definitivo pra AI Engineer hoje.
2. **"Fluent Python, 2ª ed"** — Luciano Ramalho. Para Python sólido.
3. **"Designing Machine Learning Systems"** — Chip Huyen. Mesmo sendo ML-focused, os capítulos de deploy, monitoring, e data quality aplicam direto.

Não compra outros até terminar esses 3.

---

## Anti-padrões

- **Pular Fase 2 (SDK direto) e ir direto pra LangChain.** Resultado: não consegue debugar nada quando o framework quebra.
- **Estudar sem build.** Cada bloco tem check de domínio prático. Sem o check, fase não está fechada.
- **Tutorial hell.** Mais de 3 dias num bloco sem produzir = pula pro próximo, volta depois com contexto.
- **Acumular cursos.** Termina 1 antes de começar outro. DeepLearning.AI short courses são curtos justamente pra isso.
- **Aprender PyTorch / TensorFlow / fine-tuning.** Não é teu target. Bloqueia se vier vontade.
- **Aprender Kubernetes profundo.** Lambda + Modal cobrem 95% do que precisa. K8s só se mirar enterprise sênior daqui a 2 anos.

---

## Checkpoints de revisão

- **Final da Fase 2 (Week 5):** consegues construir um chatbot com tool calling em OpenAI E Anthropic sem framework? Se não, volta.
- **Final da Fase 3 (Week 8):** tens 1 RAG production-grade rodando com eval automatizado? Esse é o **portão mais importante** do mapa.
- **Final da Fase 5 (Week 11):** tens 1 MCP server publicado? Se não, esse é o item de maior ROI — não pula.
- **Final da Fase 7 (Week 14):** consegues deployar qualquer projeto desse mapa em <30min em Lambda OU Modal? Esse é o sinal de que está job-ready.

---

## Bonus: track de inglês técnico (paralelo, 30min/dia)

Já és fluente, mas vocabulário técnico AI é específico. Forma de manter o nível alto enquanto estuda:

- Leitura: blogs em inglês listados acima (zero tradução)
- Speaking: explica conceitos em voz alta em inglês pra ti mesmo (RAG, embedding, agentic, etc.)
- Writing: README em inglês de cada projeto, posts no LinkedIn em inglês
