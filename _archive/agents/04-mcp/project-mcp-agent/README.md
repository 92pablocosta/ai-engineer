# Project — MCP-Powered Agent

## Spec

MCP server útil + agente LangGraph que consome via protocolo MCP.
Ponto-chave: agente não sabe a implementação, só o protocolo.

## MCP Server

Expõe o RAG pipeline da Etapa 02 (ou uma API real):
- `tool: search_knowledge(query, top_k)` → retrieval results
- `tool: create_document(title, content)` → add to knowledge base
- `resource: rag://corpus/stats` → corpus stats (doc count, chunk count)
- `prompt: answer_template` → parametrized prompt template

Transport: HTTP/SSE para poder rodar como serviço separado.

## Agent

LangGraph agent that:
1. Connects to MCP server via HTTP client
2. Discovers tools dynamically (via `session.list_tools()`)
3. Uses `search_knowledge` to answer questions
4. Cites sources from MCP response

## Arquitetura

```
src/mcp_agent/
  server.py    # FastMCP server (HTTP/SSE)
  client.py    # MCP client wrapper for use in agent
  agent.py     # LangGraph agent that uses MCP client as tool source
  __init__.py
```

## Definition of Done

- [ ] MCP server testável com standalone MCP client (not the agent)
- [ ] Agent discovers and calls tools via MCP protocol
- [ ] No direct import of server code in agent — protocol only
- [ ] Você explica: quando MCP vs tool calling direto?
