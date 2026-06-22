# Project — Agentic RAG

## Spec

Agente que responde sobre base de conhecimento real e densa.
pgvector + hybrid search + reranking. O agente decide quando buscar.

## Corpus

Escolha um domínio denso: documentação técnica, legislação, manual de produto.
Sugestão: documentos jurídicos do projeto de monitoramento que você já tem.

## Requisitos

- pgvector + hybrid search (BM25 + vector) + Cohere Rerank
- Agente decide se busca, re-busca se contexto insuficiente
- Respostas citam chunk de origem (doc_id + trecho)
- `EVAL.md` com recall@k e MRR no golden set

## Arquitetura

```
src/agentic_rag/
  indexer.py     # ingest + chunk + embed + store
  retriever.py   # hybrid search + reranking
  agent.py       # AgentRunner que usa retriever como tool
  __init__.py
data/
  corpus/        # raw documents
  golden_set.json
EVAL.md          # métricas de retrieval — preencher após implementar
```

## Como rodar

```bash
cp .env.example .env
# index corpus first:
uv run python -m agentic_rag.indexer --corpus data/corpus/
# then chat:
uv run python -m agentic_rag.agent "Qual o prazo para cancelamento?"
```

## Definition of Done

- [ ] Hybrid supera vector puro no golden set (número em EVAL.md)
- [ ] Reranking melhora recall@5 (número em EVAL.md)
- [ ] Agente re-busca quando retrieval insuficiente
- [ ] Toda resposta cita fonte
