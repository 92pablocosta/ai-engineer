# Project — Eval Pipeline

## Spec

Pipeline de avaliação completo para um agente existente.
Recomendação: usar o multi-agent da Etapa 03 ou RAG da Etapa 02.

## Componentes

1. **Tracing** — Langfuse self-hosted captura traces de todas as execuções
2. **Golden dataset** — 20-30 casos versionados, com critérios explícitos
3. **LLM-as-judge** — rubrica com 3 eixos (correctness, guardrail, helpfulness)
4. **Regression runner** — roda golden set, gera relatório, sai com code 1 se regride

## Arquitetura

```
src/eval_pipeline/
  tracer.py    # Langfuse integration helpers
  judge.py     # LLM-as-judge with rubric
  runner.py    # Regression suite runner
  __init__.py
data/
  golden_dataset.json   # versioned test cases
tests/
  test_judge.py
```

## Como rodar

```bash
# Run regression suite:
uv run python -m eval_pipeline.runner
# Exit 0 = pass, exit 1 = regression

# Run with Langfuse tracing:
LANGFUSE_ENABLED=true uv run python -m eval_pipeline.runner
```

## Definition of Done

- [ ] Langfuse self-hosted capturando traces
- [ ] Golden dataset com ≥20 casos, tags por tipo
- [ ] LLM judge com rubrica explícita, 3 eixos separados
- [ ] Regression runner que retorna exit code 1 em regressão
- [ ] Você mostra trace de uma falha e explica a causa raiz
