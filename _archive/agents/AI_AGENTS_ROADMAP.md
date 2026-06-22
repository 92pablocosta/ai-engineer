# AI Agents Engineering — Roadmap Build-First (2026)

> **Dono:** Pablo Costa — AI Automation Engineer (João Pessoa-PB)
> **Objetivo:** sair sabendo *fazer* agentes de IA production-grade, com portfólio que passa em screening de vaga internacional de AI Engineer.
> **Princípio:** cada etapa = conceito mínimo + build obrigatório + critério objetivo de "tá funcionando". Conceito sem código não conta como concluído.

---

## COMO USAR ESTE ARQUIVO NO CLAUDE CODE

Cole este arquivo na raiz de um repo novo (`ai-agents-lab/`) e mande pro Claude Code:

```
Leia AI_AGENTS_ROADMAP.md e crie a estrutura completa de pastas e arquivos
descrita na seção "ESTRUTURA DE DIRETÓRIOS". Para cada etapa (00 a 06):
- crie a pasta da etapa com um README.md contendo: objetivo, conceitos
  (resumidos, não copie tutorial), checklist de exercícios e a definition of done
- crie os arquivos de exercício como stubs com TODOs e docstrings, NÃO resolva
- crie a pasta do projeto da etapa com um README.md de spec e o scaffold mínimo
  (pyproject.toml ou requirements.txt, estrutura src/, tests/, .env.example)
Não implemente a lógica dos projetos — eu vou construir. Você cria o esqueleto
e os guard rails (testes vazios, type hints, estrutura).
```

Depois, em cada etapa, você abre a pasta e constrói. Use o Claude Code como par de revisão, não como autor — quem precisa sair sabendo é você.

**Regra de ouro do lab:** se o Claude Code escreveu o agente inteiro e você só leu, você não aprendeu. Implemente o core loop com as mãos pelo menos uma vez por etapa.

---

## CONTEXTO DE MERCADO (por que estas etapas, nesta ordem)

Dados de contratação de 2026, não opinião:

- **Construir agente demo virou commodity.** O sinal mais forte de contratação é conseguir *deployar, monitorar e debugar* um sistema de IA em produção — não montar um demo no notebook.
- **Eval-first é a barra de nível sênior.** Golden datasets, eval harnesses, regression testing, drift detection. A maioria dos candidatos sabe construir feature de IA mas não sabe raciocinar sobre metodologia de avaliação — e é aí que se perde a vaga premium.
- **LangGraph é o padrão de produção.** Chegou a 1.0 GA (out/2025), rodando em produção há mais de um ano em Uber, LinkedIn, Klarna. Vaga de nível médio espera que você nomeie LangGraph/CrewAI; sênior+ espera que você explique modos de falha em produção.
- **MCP (Model Context Protocol) é infraestrutura, não hype.** "USB-C da IA." Quem constrói agente em 2026 sem MCP está em stack legada.
- **RAG é o backbone** de quase todo sistema agêntico enterprise: chunking, embeddings, hybrid search (BM25 + vector), reranking, eval de retrieval (recall@k, MRR, nDCG).

**Sua vantagem injusta (não desperdice):** você já faz anotação/avaliação de IA (eval literacy — a barra sênior) e já roda VPS + Docker em produção (o sinal de contratação mais forte). O roadmap explora os dois como destino, não como apêndice.

---

## STACK 2026 (o que você vai de fato tocar)

| Camada | Ferramenta principal | Alternativa / quando usar |
|---|---|---|
| Orquestração | **LangGraph** (1.0+) | Pydantic AI (type-first, leve), Claude Agent SDK (Anthropic-native), CrewAI (protótipo role-based) |
| LLM provider | OpenAI API + Anthropic API | LiteLLM como router multi-provider |
| Structured output | **Pydantic** + JSON mode / tool calling | — |
| Vector DB | **pgvector** (você já tem Postgres) | Qdrant (standalone), depois entender Pinecone/Weaviate de nome |
| Embeddings | OpenAI `text-embedding-3-*` | modelos locais via Ollama (você já usa) |
| Reranking | Cohere Rerank / cross-encoder local | — |
| Protocolo | **MCP** (FastMCP) | A2A (agent-to-agent) de nome |
| Observability | **Langfuse** (self-host no seu VPS, open-source) | LangSmith (se for fundo no LangGraph, melhor integração) |
| Eval | Langfuse evals + RAGAS (RAG) + harness próprio | Braintrust (CI/CD eval-gated) |
| Guardrails | validação Pydantic + input/output filtering + tool approval | — |
| Deploy | **FastAPI + Docker** no seu VPS (Traefik) | você já domina isso |

> **Decisão sua (tradeoff real):** observability. **Langfuse** = open-source, self-host no seu VPS, zero custo, framework-agnóstico — combina com seu setup. **LangSmith** = integração mais profunda com LangGraph (LangGraph Studio, state diffs node-a-node, replay), mas proprietário e self-host só no Enterprise. Recomendo Langfuse pelo custo e por você já ter VPS; toque LangSmith uma vez na Etapa 3 só pra ter opinião comparativa em entrevista.

---

## ESTRUTURA DE DIRETÓRIOS

```
ai-agents-lab/
├── AI_AGENTS_ROADMAP.md          # este arquivo
├── README.md                     # índice + progresso (checklist das 7 etapas)
├── shared/
│   ├── llm_client.py             # wrapper de chamada LLM reusável (provider-agnostic)
│   ├── prompts/                  # system prompts versionados
│   └── eval_utils.py             # helpers de avaliação reusáveis
│
├── 00-foundations/
│   ├── README.md
│   ├── exercises/                # tool calling cru, structured output, ReAct na mão
│   └── project-react-agent/      # PROJETO: agente ReAct from scratch, ZERO framework
│
├── 01-agent-anatomy/
│   ├── README.md
│   ├── exercises/                # memory, tool design, retries, guardrails
│   └── project-support-agent/    # PROJETO: agente single-domain production-grade + FastAPI
│
├── 02-rag/
│   ├── README.md
│   ├── exercises/                # chunking, embeddings, hybrid search, reranking, eval retrieval
│   └── project-agentic-rag/      # PROJETO: Agentic RAG sobre base real + métricas de retrieval
│
├── 03-orchestration-langgraph/
│   ├── README.md
│   ├── exercises/                # nodes, edges, state, checkpoints, human-in-the-loop
│   ├── framework-comparison/     # mesmo agente em LangGraph vs Pydantic AI vs Claude SDK
│   └── project-multi-agent/      # PROJETO: sistema multi-agent supervisor/worker com state persistente
│
├── 04-mcp/
│   ├── README.md
│   ├── exercises/                # MCP server (tools/resources/prompts) com FastMCP
│   └── project-mcp-agent/        # PROJETO: MCP server + agente que consome via cliente
│
├── 05-eval-observability/
│   ├── README.md
│   ├── exercises/                # LLM-as-judge, golden dataset, regression suite, tracing
│   └── project-eval-pipeline/    # PROJETO: pipeline de eval + tracing pra um agente das etapas anteriores
│
├── 06-production-capstone/
│   ├── README.md
│   └── project-capstone/         # PROJETO FINAL: sistema agêntico completo, deployado, observável, com evals
│
└── interview-prep/
    ├── system-design-questions.md   # design de arquitetura agêntica
    ├── failure-modes.md             # modos de falha de produção (a pergunta sênior)
    └── talking-points.md            # como narrar cada projeto numa entrevista
```

---

## ETAPA 00 — FOUNDATIONS: o que os frameworks escondem

**Objetivo:** entender o loop de um agente construindo um *sem framework nenhum*. Isso é o que separa quem usa LangGraph de quem entende LangGraph.

**Conceitos (mínimos):**
- Tool/function calling cru via API (OpenAI/Anthropic) — o JSON schema, a roundtrip
- Structured output com Pydantic (validação > parsing de string)
- O loop ReAct: Reason → Act (tool) → Observe → repeat até resposta
- Context window, tokens, custo por chamada — por que loop sem limite = conta estourada
- Por que um agente é diferente de um chatbot: ele *decide* qual tool chamar e em que ordem

**Exercícios (`exercises/`):**
1. Chamar uma tool via API crua, sem SDK de agente. Parsear o `tool_use` block e devolver o resultado.
2. Forçar saída estruturada com Pydantic (ex: extrair `{nome, valor, data}` de um texto). Validar e tratar erro de validação.
3. Implementar retry com backoff numa chamada que falha.

**PROJETO — ReAct Agent from Scratch (`project-react-agent/`):**
Agente que responde perguntas usando 2-3 tools reais (ex: `web_search` mock, `calculator`, `read_file`). **Zero framework de agente** — só o SDK do LLM + Python. Loop ReAct escrito na mão, com:
- limite máximo de iterações (anti-loop infinito)
- logging de cada passo (reason/action/observation)
- tratamento de erro quando a tool falha
- contagem de tokens/custo por execução

> Por que faz sentido pra empresa: prova que você entende o que acontece *embaixo* do framework. Em entrevista, "construí o loop ReAct na mão antes de usar LangGraph" é um sinal forte.

**Definition of Done:**
- [ ] o agente resolve uma pergunta multi-step que exige 2+ tool calls encadeadas
- [ ] não entra em loop infinito (limite testado)
- [ ] loga reason/action/observation de cada passo
- [ ] você consegue explicar, sem olhar, o que o framework vai abstrair disso

---

## ETAPA 01 — ANATOMIA DE UM AGENTE PRODUCTION-GRADE

**Objetivo:** transformar o loop cru numa coisa que não quebra na cara do usuário. Single-agent, mas robusto.

**Conceitos (mínimos):**
- Memory: short-term (histórico da conversa) vs long-term (persistência entre sessões)
- Tool design: descrições claras, schemas tipados, idempotência, o que NÃO fazer uma tool fazer
- Guardrails: validação de input, validação de output, aprovação humana pra ação de alto risco
- Error handling: retry, fallback, degradação graciosa (quando a tool morre, o agente não morre junto)
- Quando NÃO usar agente: se um workflow determinístico resolve, agente é over-engineering caro

**Exercícios (`exercises/`):**
1. Adicionar memory persistente (SQLite/Postgres) ao agente da Etapa 00.
2. Escrever 3 tools com schemas Pydantic tipados e descrições que o LLM não interpreta errado.
3. Implementar um guardrail de output: o agente nunca devolve dado sensível / nunca executa ação destrutiva sem confirmação.

**PROJETO — Support Agent + FastAPI (`project-support-agent/`):**
Agente de atendimento de um domínio real (ex: FAQ + ações de uma clínica — você tem o DentBot como referência de domínio). Expõe via **FastAPI**, deploya no seu VPS via Docker.
- memory por sessão (Postgres)
- 3-4 tools reais (consultar disponibilidade, criar lembrete, escalar pra humano)
- guardrail: ação de "agendar/cancelar" exige confirmação
- endpoint `/health` e tratamento de erro que retorna mensagem útil, não stack trace

> Por que faz sentido pra empresa: é um agente que *deployou* e tem guardrails — o oposto de demo de notebook. Conecta com seu trabalho real (WhatsApp AI), mas reescrito como serviço HTTP limpo.

**Definition of Done:**
- [ ] roda como serviço FastAPI dockerizado (no seu VPS, idealmente)
- [ ] mantém contexto entre mensagens da mesma sessão
- [ ] tem pelo menos 1 guardrail de ação de alto risco testado
- [ ] quando uma tool falha, o usuário recebe resposta útil (não erro 500)

---

## ETAPA 02 — RAG: o backbone

**Objetivo:** dar ao agente conhecimento que não está no modelo, e saber *medir* se o retrieval está bom. RAG ruim mata mais sistema agêntico que LLM ruim.

**Conceitos (mínimos):**
- Embeddings: o que são, como escolher modelo, dimensionalidade
- Chunking strategies: fixed-size, recursive, semantic — e por que chunk errado destrói recall
- Vector search vs keyword search; **hybrid search (BM25 + vector)** e por que ganha de só vector
- Reranking: cross-encoder / Cohere Rerank pra cortar o lixo do top-k
- Eval de retrieval (CRÍTICO): **recall@k, MRR, nDCG** — sem isso você está chutando
- Agentic RAG: agente decide *se* busca, busca de novo se faltou contexto, valida fontes (vs RAG clássico "busca uma vez e resume")

**Exercícios (`exercises/`):**
1. Indexar um corpus em **pgvector** (você já tem Postgres). Busca por similaridade top-k.
2. Implementar hybrid search (BM25 + vector) e comparar resultados com vector puro no mesmo query set.
3. Adicionar reranking e medir recall@5 antes/depois.
4. Montar um golden set de 20 perguntas→docs corretos e calcular recall@k e MRR.

**PROJETO — Agentic RAG (`project-agentic-rag/`):**
Agente que responde sobre uma base de conhecimento real e densa (ex: documentação técnica, legislação, manual de produto — você tem o domínio jurídico do projeto de monitoramento como opção). 
- pgvector + hybrid search + reranking
- o agente decide quando buscar e re-busca se o contexto for insuficiente
- cita as fontes (chunk → doc origem)
- **relatório de métricas de retrieval** (recall@k, MRR) num `EVAL.md`

> Por que faz sentido pra empresa: RAG é o que mais aparece em vaga. E você não só construiu — você *mediu*. Em 2026, mostrar recall@k de um sistema seu é o que separa de quem só seguiu tutorial.

**Definition of Done:**
- [ ] hybrid search supera vector puro no seu golden set (com número provando)
- [ ] reranking melhora recall@5 (com número provando)
- [ ] o agente re-busca quando o primeiro retrieval é insuficiente
- [ ] respostas citam a fonte; existe `EVAL.md` com as métricas

---

## ETAPA 03 — ORQUESTRAÇÃO COM LANGGRAPH (o framework que contrata)

**Objetivo:** sair fluente em LangGraph e ter opinião comparativa sobre os concorrentes. Esta é a etapa que mais aparece na descrição de vaga.

**Conceitos (mínimos):**
- Grafo dirigido: nodes (agentes/tools/checkpoints), edges (condicionais), state explícito
- State management e reducers (merge de updates concorrentes)
- Checkpoints e persistência de estado (durable execution)
- Human-in-the-loop: pausar o grafo, esperar aprovação, retomar
- Multi-agent patterns: supervisor/worker, handoffs entre agentes
- Modos de falha em produção (a pergunta sênior): tool-call retry loops, custo de loop descontrolado, prompt regression em upgrade de modelo

**Exercícios (`exercises/`):**
1. Reconstruir o agente da Etapa 01 em LangGraph (nodes + edges condicionais + state).
2. Adicionar um checkpoint que persiste o state e permite retomar uma execução interrompida.
3. Adicionar human-in-the-loop num node de ação de alto risco.

**Comparação de frameworks (`framework-comparison/`):**
Mesmo agente simples (ex: triagem de email: classifica urgente/normal/spam, rascunha resposta, escala urgente) implementado em **LangGraph**, **Pydantic AI** e **Claude Agent SDK**. Escreva um `COMPARISON.md`: linhas de código, controle de fluxo, persistência, quando você escolheria cada um.

**PROJETO — Multi-Agent System (`project-multi-agent/`):**
Sistema supervisor/worker: um supervisor roteia tarefas pra agentes especialistas (ex: um pesquisa, um escreve, um revisa). State persistente, human-in-the-loop antes da ação final.
- supervisor com roteamento condicional
- 2-3 worker agents especializados
- state que sobrevive a restart (checkpoint)
- ponto de aprovação humana

> Por que faz sentido pra empresa: multi-agent supervisor/worker é literalmente o que a descrição da vaga sênior pede ("designing multi-agent systems with supervisor and worker patterns, managing state across tool calls").

**Definition of Done:**
- [ ] o multi-agent roda em LangGraph com state persistente (sobrevive a restart)
- [ ] tem human-in-the-loop funcional
- [ ] existe `COMPARISON.md` com sua opinião fundamentada LangGraph vs Pydantic AI vs Claude SDK
- [ ] você consegue explicar 3 modos de falha em produção desse sistema

---

## ETAPA 04 — MCP (Model Context Protocol)

**Objetivo:** dominar o protocolo que virou padrão de integração de agentes. Você já fez um MCP server — aqui você aprofunda e conecta a um agente real.

**Conceitos (mínimos):**
- O que MCP resolve: padronizar como agentes acessam tools/dados/prompts (o "USB-C")
- Os 3 primitivos: **tools** (ações), **resources** (dados), **prompts** (templates)
- Server vs client; transporte (stdio, HTTP/SSE)
- FastMCP pra construir servers em Python rápido
- Quando MCP vs tool calling direto

**Exercícios (`exercises/`):**
1. Construir um MCP server com FastMCP expondo 2 tools e 1 resource.
2. Conectar via cliente MCP e listar/chamar as tools.
3. Expor um dos sistemas de etapas anteriores (ex: o RAG da Etapa 02) como um MCP resource.

**PROJETO — MCP-Powered Agent (`project-mcp-agent/`):**
Um MCP server útil (ex: acesso ao seu RAG, ou a uma API real) + um agente LangGraph que consome esse server via MCP. O ponto é a interoperabilidade: o agente não sabe a implementação, só o protocolo.

> Por que faz sentido pra empresa: você entrevistou pra role de MCP/FastMCP. Ter um MCP server + agente consumidor no portfólio é prova direta. MCP em 2026 é diferenciador de contratação.

**Definition of Done:**
- [ ] MCP server com tools + resources funcionando, testável via cliente
- [ ] um agente consome o server via protocolo MCP (não import direto)
- [ ] você consegue explicar quando usaria MCP vs tool calling direto

---

## ETAPA 05 — EVAL & OBSERVABILITY (seu diferencial / a barra sênior)

**Objetivo:** a etapa que te coloca acima de 90% dos candidatos. Você já tem eval literacy da anotação — aqui vira engenharia.

**Conceitos (mínimos):**
- Por que eval de agente ≠ eval de LLM: falha de agente aparece em cadeia causal multi-step, não numa chamada isolada — precisa de trace de sessão inteira
- **Golden dataset**: casos de entrada→saída esperada, versionado
- **LLM-as-judge**: usar um modelo pra avaliar saídas (cuidado com seus vieses conhecidos: score inflation, misturar eixos, justificativa vaga)
- **Eval harness = regression test suite**: task-level success, latency, cost — roda a cada mudança de prompt
- Tracing: capturar cada passo (LLM call, tool, retrieval, decisão de planning)
- Drift detection: a saída piora silenciosamente com o tempo / upgrade de modelo
- Span-attached eval: o score vive no span do trace, não num dashboard separado

**Exercícios (`exercises/`):**
1. Instrumentar um agente das etapas anteriores com **Langfuse** (self-host no seu VPS).
2. Montar um golden dataset de 20-30 casos pra um dos seus agentes.
3. Escrever um LLM-as-judge com rubrica explícita (aplique sua disciplina de anotação: eixos separados, sem inflar nota).
4. Montar um regression suite que roda o golden set e falha se success rate cair X%.

**PROJETO — Eval Pipeline (`project-eval-pipeline/`):**
Pipeline de avaliação completo pra um dos agentes (recomendo o multi-agent da Etapa 03 ou o RAG da Etapa 02):
- tracing com Langfuse (cada execução logada)
- golden dataset versionado
- LLM-as-judge com rubrica + métricas determinísticas (latency, cost, success)
- regression report: rodou, X% passou, regrediu em quê

> Por que faz sentido pra empresa: "candidatos que constroem feature de IA mas não raciocinam sobre eval perdem as vagas premium." Você inverte isso. Um eval pipeline real no portfólio é o sinal mais raro e mais valorizado.

**Definition of Done:**
- [ ] Langfuse self-hosted capturando traces dos seus agentes
- [ ] golden dataset versionado + LLM-as-judge com rubrica
- [ ] regression suite que detecta queda de qualidade automaticamente
- [ ] você consegue mostrar um trace e apontar onde/por que um agente falhou

---

## ETAPA 06 — PRODUCTION CAPSTONE

**Objetivo:** juntar tudo num sistema que você poderia colocar no ar pra um cliente/empresa amanhã. É o projeto que vai no topo do GitHub e do LinkedIn.

**Conceitos (mínimos):**
- Cost & latency management: caching, escolha de modelo por tarefa, streaming
- Guardrails de produção: OWASP LLM Top 10 (prompt injection, data leakage, etc)
- Multi-provider failover (LiteLLM)
- Deploy + monitoring contínuo (você já domina Docker/VPS/Traefik)

**PROJETO — Sistema Agêntico Completo (`project-capstone/`):**
Escolha UM domínio real e vertical (sugestão alinhada ao seu portfólio: assistente jurídico de monitoramento, ou agente de atendimento+agendamento de clínica). Tem que ter:
- multi-agent (LangGraph) com state persistente
- RAG (pgvector, hybrid, reranking) sobre base real
- pelo menos um MCP server
- guardrails de produção
- observability (Langfuse) + eval pipeline com regression suite
- deployado no VPS, dockerizado, com `/health` e tratamento de erro
- README com arquitetura (diagrama), decisões de design, métricas de eval, e modos de falha conhecidos

> Por que faz sentido pra empresa: é a prova de que você fecha o ciclo inteiro — construir, deployar, medir, debugar. O README com "modos de falha conhecidos" e métricas é o que faz um recrutador sênior parar de rolar a tela.

**Definition of Done:**
- [ ] no ar, acessível, dockerizado no seu VPS
- [ ] tem RAG + multi-agent + MCP + guardrails + eval, todos funcionando juntos
- [ ] README com diagrama de arquitetura, decisões, métricas e modos de falha
- [ ] você consegue dar um walkthrough de 10 min explicando cada decisão

---

## INTERVIEW PREP (paralelo, não no fim)

A partir da Etapa 03, mantenha `interview-prep/` vivo:
- **`failure-modes.md`**: pra cada projeto, liste como ele falha em produção e como você mitigaria. Esta é A pergunta de nível sênior.
- **`system-design-questions.md`**: pratique desenhar arquitetura agêntica no papel (supervisor/worker, onde entra RAG, onde entra eval, cost/latency).
- **`talking-points.md`**: 1 parágrafo por projeto narrando o problema de negócio → sua solução → o que mediu → o que aprendeu. Em inglês (você é fluente — use isso, é diferencial pra vaga internacional).

---

## SEQUÊNCIA E PRIORIDADE

Ordem obrigatória: 00 → 01 → 02 → 03. Essas são fundação e não pulam.

A partir daí, **04 (MCP) e 05 (Eval) são seus aceleradores de contratação** dado seu perfil (entrevista de MCP + eval literacy) — não deixe pro fim. Se tiver que escolher entre fazer mais um projeto de agente ou montar o eval pipeline, **faça o eval**. É o que ninguém faz e o que mais te diferencia.

06 (Capstone) é o que você aponta no LinkedIn e no GitHub. Não comece antes de ter 02, 03 e 05 sólidas — senão vira mais um demo.

**Não otimize por quantidade de projetos.** Três projetos com eval, deploy e modos de falha documentados valem mais que dez demos. O mercado de 2026 premia profundidade, não menu.
