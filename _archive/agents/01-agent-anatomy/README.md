# Stage 01 — Anatomia de um Agente Production-Grade

## Objetivo

Transformar o loop cru numa coisa que não quebra na cara do usuário.
Single-agent robusto com memory, guardrails, e deploy real.

## Conceitos

- **Memory**: short-term (histórico da conversa em RAM) vs long-term (Postgres entre sessões)
- **Tool design**: descrição clara que o LLM não interpreta errado; schema tipado; idempotência
- **Guardrails**: validar input do usuário; validar output antes de entregar; ação de alto risco = confirmação humana
- **Error handling**: tool que morre não mata o agente — graceful degradation
- **Quando NÃO usar agente**: workflow determinístico resolve mais barato e mais rápido

## Exercícios

- [ ] `exercises/01_persistent_memory.py` — adicionar SQLite/Postgres memory ao agente da Etapa 00
- [ ] `exercises/02_typed_tools.py` — 3 tools com schemas Pydantic + descrições não-ambíguas
- [ ] `exercises/03_output_guardrail.py` — guardrail que bloqueia dado sensível / ação destrutiva sem confirmação

## Definition of Done

- [ ] Roda como serviço FastAPI dockerizado (no VPS idealmente)
- [ ] Mantém contexto entre mensagens da mesma sessão
- [ ] Pelo menos 1 guardrail de ação de alto risco testado
- [ ] Tool que falha → usuário recebe resposta útil, não erro 500
