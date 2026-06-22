"""Exercise 01 — Rebuild support agent in LangGraph.

Goal: understand how LangGraph abstracts the ReAct loop.
  1. Define State TypedDict with messages and tool_calls.
  2. Create nodes: call_llm, execute_tools.
  3. Add conditional edge: if response has tool_calls → tools, else → END.
  4. Compile and run with the same queries as Etapa 01.
  5. Compare: what did LangGraph hide vs your manual loop?

Run: uv run python exercises/01_langgraph_basic.py
"""

from __future__ import annotations

from typing import Annotated, TypedDict
import operator

# from langgraph.graph import StateGraph, END
# from langchain_anthropic import ChatAnthropic


class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    # TODO: add any extra state fields you need


def call_llm_node(state: AgentState) -> dict:
    """Call LLM with current messages. Return {messages: [new_message]}."""
    # TODO: implement
    raise NotImplementedError


def execute_tools_node(state: AgentState) -> dict:
    """Execute tool calls from last message. Return {messages: [tool_result_messages]}."""
    # TODO: implement
    raise NotImplementedError


def should_continue(state: AgentState) -> str:
    """Conditional edge: 'tools' if last message has tool_calls, else 'end'."""
    # TODO: check state["messages"][-1].tool_calls
    raise NotImplementedError


def build_graph():
    """Build and compile the LangGraph agent."""
    # TODO:
    # graph = StateGraph(AgentState)
    # graph.add_node("llm", call_llm_node)
    # graph.add_node("tools", execute_tools_node)
    # graph.set_entry_point("llm")
    # graph.add_conditional_edges("llm", should_continue, {"tools": "tools", "end": END})
    # graph.add_edge("tools", "llm")
    # return graph.compile()
    raise NotImplementedError


if __name__ == "__main__":
    graph = build_graph()
    result = graph.invoke({"messages": [{"role": "user", "content": "Qual o horário de atendimento?"}]})
    print(result["messages"][-1].content)
