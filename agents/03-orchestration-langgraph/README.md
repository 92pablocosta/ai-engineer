# Stage 03 — Orquestração com LangGraph

## Objetivo

Sair fluente em LangGraph e ter opinião comparativa sobre os concorrentes.
A etapa que mais aparece em descrição de vaga.

## Conceitos

- **Grafo dirigido**: nodes (agentes/tools/functions), edges condicionais, state explícito e tipado
- **State + reducers**: como updates concorrentes são merged; por que `Annotated[list, operator.add]` importa
- **Checkpoints**: durable execution — estado sobrevive a restart, permite replay
- **Human-in-the-loop**: pausar o grafo em um node, esperar input externo, retomar
- **Multi-agent patterns**: supervisor roteia pra workers, handoffs via state
- **Modos de falha em produção**: tool-call retry loops, custo descontrolado, prompt regression em upgrade de modelo

## Exercícios

- [ ] `exercises/01_langgraph_basic.py` — reconstruir agente da Etapa 01 em LangGraph (nodes + conditional edges)
- [ ] `exercises/02_checkpoints.py` — adicionar checkpoint, pausar, retomar execução interrompida
- [ ] `exercises/03_human_in_loop.py` — node de ação de alto risco que espera aprovação humana

## Framework Comparison

`framework-comparison/` — mesmo agente em LangGraph, Pydantic AI e Claude Agent SDK.
Escrever `COMPARISON.md` com: linhas de código, controle de fluxo, persistência, quando escolher cada um.

## Definition of Done

- [ ] Multi-agent roda em LangGraph com state persistente (sobrevive restart)
- [ ] Human-in-the-loop funcional
- [ ] `COMPARISON.md` com opinião fundamentada LangGraph vs Pydantic AI vs Claude SDK
- [ ] Você consegue explicar 3 modos de falha em produção desse sistema
