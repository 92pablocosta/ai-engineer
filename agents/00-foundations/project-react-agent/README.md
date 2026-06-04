# Project — ReAct Agent from Scratch

## Spec

Agente que responde perguntas usando 2-3 tools reais.
**Zero framework de agente** — só SDK do LLM + Python.

## Tools

- `calculator(expression: str) -> float` — avalia expressão matemática
- `web_search(query: str) -> str` — mock: retorna snippets hardcoded
- `read_file(path: str) -> str` — lê arquivo local (sandbox: só `data/`)

## Requisitos

- Loop ReAct na mão: Reason → Act → Observe → repeat
- Limite máximo de iterações configurável (`MAX_ITER`, default 10)
- Log estruturado de cada passo: `{step, type: reason|action|observation, content}`
- Contagem de tokens + custo estimado por execução
- Quando tool falha: agent recebe o erro como observation e decide o que fazer

## Arquitetura

```
src/react_agent/
  agent.py     # AgentRunner: loop principal
  tools.py     # tool implementations + registry
  loop.py      # ReActStep dataclass, step logger
  __init__.py
```

## Como rodar

```bash
uv sync
uv run python -m react_agent "Qual é a raiz quadrada de 144 mais 7?"
```

## Definition of Done

- [ ] resolve pergunta multi-step com 2+ tool calls encadeadas
- [ ] MAX_ITER testado — para e loga quando atingido
- [ ] cada passo logado (reason / action / observation)
- [ ] custo total impresso ao final
