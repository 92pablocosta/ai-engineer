# Stage 02 — RAG: o backbone

## Objetivo

Dar ao agente conhecimento fora do modelo e *medir* se o retrieval está bom.
RAG ruim mata mais sistema agêntico que LLM ruim.

## Conceitos

- **Embeddings**: representação vetorial de semântica; escolha de modelo afeta recall
- **Chunking**: tamanho e estratégia (fixed/recursive/semantic) determinam o que o retrieval encontra
- **Hybrid search**: BM25 (keyword) + vector — supera vector puro em benchmarks, especialmente para termos técnicos
- **Reranking**: cross-encoder ou Cohere Rerank filtra o lixo do top-k antes de passar pro LLM
- **Eval de retrieval**: recall@k, MRR, nDCG — sem isso você está chutando
- **Agentic RAG**: agente decide *quando* buscar, re-busca se contexto insuficiente, valida fontes

## Exercícios

- [ ] `exercises/01_pgvector_index.py` — indexar corpus em pgvector, busca por similaridade top-k
- [ ] `exercises/02_hybrid_search.py` — BM25 + vector, comparar resultados no mesmo query set
- [ ] `exercises/03_reranking.py` — adicionar reranking, medir recall@5 antes/depois
- [ ] `exercises/04_golden_set_eval.py` — golden set de 20 perguntas, calcular recall@k e MRR

## Definition of Done

- [ ] Hybrid search supera vector puro no golden set (número provando)
- [ ] Reranking melhora recall@5 (número provando)
- [ ] Agente re-busca quando primeiro retrieval é insuficiente
- [ ] Respostas citam fonte; existe `EVAL.md` com métricas
