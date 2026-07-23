from openai import OpenAI

client = OpenAI()   

# text -> embedding
def get_embedding(text: str) -> list[float]:
    """
    Generate an embedding for the provided text.

    Args:
        text: Input text.
    
    Returns:
        Embedding vector.
    """

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding
