# Project — Support Agent + FastAPI

## Spec

Agente de atendimento de domínio único (clínica / DentBot reference domain).
Exposto via FastAPI, deployado no VPS via Docker.

## Domínio

Clínica odontológica. Tools:
- `check_availability(doctor_id, date)` → slots disponíveis
- `create_reminder(patient_id, appointment_id, message)` → agenda lembrete
- `get_faq(topic)` → responde dúvidas comuns
- `escalate_to_human(reason)` → flag para atendente humano

## Requisitos

- Memory por sessão em Postgres (não SQLite — produção exige Postgres)
- Guardrail: ações de agendar/cancelar exigem confirmação explícita
- `/health` endpoint retorna `{"status": "ok", "db": "ok"}`
- Quando tool falha: resposta útil para usuário, erro logado internamente

## API

```
POST /chat
  Body: {"session_id": "uuid", "message": "string"}
  Response: {"reply": "string", "session_id": "uuid"}

GET  /health
  Response: {"status": "ok", "db": "ok"}
```

## Arquitetura

```
src/support_agent/
  agent.py       # AgentRunner com memory
  tools.py       # 4 tools com Pydantic schemas
  memory.py      # Postgres session store
  guardrails.py  # PII + action guardrails
  api.py         # FastAPI app
  __init__.py
```

## Como rodar

```bash
cp .env.example .env  # preencher DATABASE_URL e ANTHROPIC_API_KEY
docker compose up
# ou local:
uv sync && uv run uvicorn support_agent.api:app --reload
```

## Definition of Done

- [ ] FastAPI dockerizado rodando (local ou VPS)
- [ ] Contexto persiste entre mensagens da mesma sessão
- [ ] Guardrail de cancelamento testado
- [ ] Tool que lança exceção → usuário recebe mensagem amigável
