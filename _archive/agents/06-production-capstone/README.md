# Stage 06 — Production Capstone

## Objetivo

Juntar tudo num sistema que você poderia colocar no ar pra um cliente amanhã.
É o projeto que vai no topo do GitHub e do LinkedIn.

## Conceitos finais

- **Cost & latency management**: caching de prompt, escolha de modelo por tarefa (Haiku pra classificação, Opus pra raciocínio), streaming
- **OWASP LLM Top 10**: prompt injection, data leakage, insecure output handling — pelo menos os 3 primeiros
- **Multi-provider failover**: LiteLLM como router (Anthropic primário, OpenAI fallback)
- **Deploy + monitoring**: Docker + Traefik + Langfuse no VPS — você já domina isso

## Quando começar

Não antes de ter 02, 03 e 05 sólidas. Sem isso vira mais um demo.

## Projeto

Ver `project-capstone/README.md` para spec completa.
