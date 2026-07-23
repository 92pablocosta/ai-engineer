from embeddings import get_embedding

text = "Python is a programming language."

if not text.strip():
    raise ValueError("Text cannot be empty.")

embedding = get_embedding(text)

print(type(embedding))
print(len(embedding))
print(embedding[:10])
