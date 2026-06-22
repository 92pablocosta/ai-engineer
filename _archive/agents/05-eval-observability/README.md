# Stage 05 — Eval & Observability

## Objetivo

A etapa que coloca acima de 90% dos candidatos.
Eval literacy da anotação vira engenharia.

## Conceitos

- **Eval de agente ≠ eval de LLM**: falha aparece em cadeia causal multi-step — precisa de trace de sessão inteira, não chamada isolada
- **Golden dataset**: casos input→output esperado versionados como código; evolui como os testes
- **LLM-as-judge**: cuidados: score inflation, misturar eixos, justificativa vaga — use rubrica explícita com eixos separados
- **Eval harness**: roda golden set a cada mudança de prompt, falha se success rate cair X%
- **Tracing**: cada LLM call, tool call, retrieval, decisão de planning vira um span
- **Drift detection**: qualidade piora silenciosamente — regression suite detecta antes do usuário

## Exercícios

- [ ] `exercises/01_langfuse_tracing.py` — instrumentar agente com Langfuse (self-host no VPS)
- [ ] `exercises/02_golden_dataset.py` — 20-30 casos para um dos seus agentes
- [ ] `exercises/03_llm_judge.py` — LLM-as-judge com rubrica explícita (eixos separados, sem inflar nota)
- [ ] `exercises/04_regression_suite.py` — suite que roda golden set, falha se success rate cair X%

## Definition of Done

- [ ] Langfuse self-hosted capturando traces dos agentes
- [ ] Golden dataset versionado + LLM-as-judge com rubrica
- [ ] Regression suite detecta queda de qualidade automaticamente
- [ ] Você mostra trace e aponta onde/por que um agente falhou
