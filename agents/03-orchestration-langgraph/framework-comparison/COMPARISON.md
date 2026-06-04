# Framework Comparison: LangGraph vs Pydantic AI vs Claude Agent SDK

Same agent implemented 3 ways: email triage (classify urgent/normal/spam, draft reply, escalate urgent).

## Implementations

- `langgraph_agent.py`
- `pydantic_ai_agent.py`
- `claude_sdk_agent.py`

## Comparison Table

| Dimension | LangGraph | Pydantic AI | Claude SDK |
|-----------|-----------|-------------|------------|
| Lines of code | — | — | — |
| State management | explicit TypedDict | typed model | dict |
| Persistence | SqliteSaver/PostgresSaver built-in | manual | manual |
| Human-in-the-loop | interrupt_before native | manual | manual |
| Multi-agent | supervisor/worker native | manual | manual |
| Type safety | partial | strict (mypy friendly) | loose |
| Learning curve | steep | moderate | low |
| Vendor lock-in | LangChain ecosystem | none | Anthropic |

## When I'd choose each

_Fill this in after building all three._

**LangGraph**: 

**Pydantic AI**: 

**Claude SDK**: 

## Failure modes I found

_Fill in during implementation — the hard-won learnings are the valuable part._
