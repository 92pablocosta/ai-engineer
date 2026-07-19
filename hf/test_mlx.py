from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Llama-3.2-3B-Instruct-4bit")


prompt = str(input(">>"))
messages = [
    {"role": "system", "content": "Você é o assistente de Pablo Costa."},
    {"role": "user", "content": prompt}
    ]
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

response = generate(
    model,
    tokenizer,
    prompt=prompt,
    max_tokens=500,
    verbose=True,
)

print(response)
