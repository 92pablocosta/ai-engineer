# Stage 00 — Foundations: o que os frameworks escondem

## Objetivo

Entender o loop de um agente construindo um *sem framework nenhum*.
Quem usa LangGraph sem ter feito isso está operando no escuro.

## Conceitos

- **Tool/function calling cru**: JSON schema → API → parse `tool_use` block → devolver resultado
- **Structured output com Pydantic**: validação > parsing de string; tratar `ValidationError`
- **Loop ReAct**: Reason → Act (tool call) → Observe → repeat. Tem que ter limite de iterações.
- **Context window + custo**: cada iteração custa tokens. Loop sem limite = conta estourada.
- **Agente ≠ chatbot**: agente *decide* qual tool chamar e em que ordem. Chatbot só responde.

## Exercícios

- [ ] `exercises/01_tool_calling_raw.py` — chamar tool via API crua, parsear resposta, devolver resultado
- [ ] `exercises/02_structured_output.py` — extrair struct tipada de texto, tratar ValidationError
- [ ] `exercises/03_retry_backoff.py` — retry com exponential backoff em chamada que falha

## Definition of Done

- [ ] Agente resolve pergunta multi-step com 2+ tool calls encadeadas
- [ ] Não entra em loop infinito (limite de iterações testado e logado)
- [ ] Loga reason/action/observation de cada passo
- [ ] Você consegue explicar, sem olhar, o que LangGraph vai abstrair disso
