# Project — Production Capstone

## Spec

Sistema agêntico completo, deployado, observável, com evals.
Escolha UM domínio real. Sugestões:
- Assistente jurídico de monitoramento (você tem o domínio)
- Agente de atendimento + agendamento de clínica (DentBot, reescrito como serviço limpo)

## Requisitos mandatórios

- [ ] Multi-agent (LangGraph) com state persistente
- [ ] RAG (pgvector, hybrid search, reranking) sobre base real
- [ ] Pelo menos 1 MCP server
- [ ] Guardrails de produção (OWASP LLM Top 10 primeiros 3)
- [ ] Observability (Langfuse) + eval pipeline com regression suite
- [ ] Deployado no VPS, dockerizado, com `/health` e tratamento de erro
- [ ] README com diagrama de arquitetura, decisões de design, métricas de eval, modos de falha conhecidos

## Arquitetura (preencher ao projetar)

```
[desenhar aqui antes de implementar]
```

## Decisões de design

_Preencher: por que LangGraph? Por que pgvector e não Qdrant? Por que este chunking strategy?_

## Métricas de eval

_Preencher após implementar_

| Metric | Value |
|--------|-------|
| Retrieval recall@5 | — |
| LLM judge overall (p50) | — |
| Regression suite pass rate | — |
| p95 latency | — |
| Cost per session (avg) | — |

## Modos de falha conhecidos

_Preencher — isto é o que faz um recrutador sênior parar de rolar a tela._

1. **[Failure mode]**: [description] → [mitigation]
2. ...

## Como rodar

```bash
cp .env.example .env
docker compose up
# Access: http://localhost:8000
# Langfuse: http://localhost:3000
```

## Walkthrough (10 min)

_Estruturar aqui: problema de negócio → solução → o que medi → o que aprendi._
