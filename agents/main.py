import anthropic

client = anthropic.Anthropic()

TOOLS = [
    {
        "name": "get_weather",
        "description": "Retorna o clima atual de uma cidade.",
        "input_schema": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    }
]

def execute_tool(name: str, args: dict) -> str:
    if name == "get_weather":
        return f"Clima em {args['city']}: 28°C, ensolarado."
    return "Tool desconhecida."

def run_agent(user_message: str, max_iterations: int = 10) -> str:
    messages = [{"role": "user", "content": user_message}]

    for _ in range(max_iterations):          # SEMPRE limite o loop
        response = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=1024,
            tools=TOOLS,
            messages=messages,
        )

        # Sem tool call -> agente terminou
        if response.stop_reason != "tool_use":
            return "".join(b.text for b in response.content if b.type == "text")

        # Registra o turno do assistant (thoughts + tool calls)
        messages.append({"role": "assistant", "content": response.content})

        # ACT: executa cada tool pedida
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = execute_tool(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                })

        # OBSERVE: devolve resultados e fecha o ciclo
        messages.append({"role": "user", "content": tool_results})

    return "Atingiu o limite de iterações."
