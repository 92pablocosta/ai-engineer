"""Provider-agnostic LLM client wrapper.

Wraps OpenAI and Anthropic SDKs behind a single interface.
Tracks token usage and cost per call.
"""

from __future__ import annotations

from typing import Any

# TODO: implement LLMClient class
# - __init__(provider: "openai" | "anthropic", model: str, ...)
# - chat(messages: list[dict], tools: list[dict] | None = None) -> LLMResponse
# - LLMResponse: content, tool_calls, input_tokens, output_tokens, cost_usd
# - cost_usd calculation per model (hard-code a pricing table)
# - structured_output(messages, response_model: type[BaseModel]) -> BaseModel
