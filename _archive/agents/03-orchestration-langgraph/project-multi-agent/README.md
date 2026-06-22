# Project — Multi-Agent System (LangGraph)

## Spec

Supervisor que roteia tarefas para agentes especialistas.
State persistente, human-in-the-loop antes da ação final.

## Agentes

- **Supervisor**: recebe tarefa do usuário, decide qual worker chamar
- **Researcher**: busca informação (pode usar RAG da Etapa 02)
- **Writer**: produz rascunho baseado em pesquisa
- **Reviewer**: revisa e aprova ou devolve para Writer

## Fluxo

```
User → Supervisor → Researcher → Writer → [Human Approval] → Reviewer → Output
                 ↑__________________|  (se revisor pede reescrita)
```

## Requisitos

- State sobrevive a restart (PostgresSaver ou SqliteSaver)
- Human-in-the-loop antes de entrega final (interrupt_before)
- Supervisor usa conditional routing — não chama todos os workers sempre
- Cada worker é um subgraph ou node com tools próprias

## Arquitetura

```
src/multi_agent/
  state.py      # AgentState TypedDict + reducers
  supervisor.py # Supervisor node + routing logic
  workers.py    # Researcher, Writer, Reviewer nodes
  graph.py      # assemble full graph + compile
  __init__.py
```

## Definition of Done

- [ ] Fluxo completo roda em LangGraph com state persistente
- [ ] Human-in-the-loop funcional (graph pausa, aguarda, retoma)
- [ ] State sobrevive restart (testar: matar processo, retomar com thread_id)
- [ ] Você consegue nomear 3 modos de falha em produção deste sistema
