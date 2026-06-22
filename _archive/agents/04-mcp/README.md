# Stage 04 — MCP (Model Context Protocol)

## Objetivo

Dominar o protocolo que virou padrão de integração de agentes.
Você já fez um MCP server — aqui aprofunda e conecta a agente real.

## Conceitos

- **O que MCP resolve**: padroniza como agentes acessam tools/dados/prompts — "USB-C da IA"
- **3 primitivos**: tools (ações), resources (dados leitura), prompts (templates parametrizados)
- **Transport**: stdio (local), HTTP/SSE (remoto) — stdio pra dev, HTTP pra produção
- **FastMCP**: abstração Python que elimina boilerplate do protocolo MCP
- **MCP vs tool calling direto**: MCP = interoperabilidade multi-client; tool calling = acoplado ao agente

## Exercícios

- [ ] `exercises/01_mcp_server.py` — MCP server FastMCP com 2 tools + 1 resource
- [ ] `exercises/02_mcp_client.py` — conectar via cliente MCP, listar tools, chamar uma
- [ ] `exercises/03_rag_as_resource.py` — expor RAG da Etapa 02 como MCP resource

## Definition of Done

- [ ] MCP server com tools + resources funcionando, testável via cliente MCP
- [ ] Agente consome o server via protocolo MCP (não import direto)
- [ ] Você consegue explicar quando usaria MCP vs tool calling direto
