import os

from dotenv import load_dotenv
from openai import OpenAI
from openai import APIConnectionError, APIStatusError, RateLimitError

load_dotenv()

EMBEDDING_MODEL = "text-embedding-3-small"

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY was not found. " "Add it to the .env file.")

client = OpenAI(api_key=api_key)


def get_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for multiple texts in a single API request.

    Args:
        texts: List of non-empty texts.

    Returns:
        List of embedding vectors in the same order as the input texts.

    Raises:
        ValueError: If the list is empty or contains empty texts.
        RuntimeError: If the OpenAI API request fails.
    """
    if not texts:
        raise ValueError("Texts list cannot be empty.")

    normalized_texts = [text.strip() for text in texts]

    if any(not text for text in normalized_texts):
        raise ValueError("Texts cannot contain empty values.")

    try:
        response = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=normalized_texts,
        )

        sorted_data = sorted(
            response.data,
            key=lambda item: item.index,
        )

        return [item.embedding for item in sorted_data]

    except RateLimitError as error:
        raise RuntimeError("OpenAI rate limit exceeded. Try again later.") from error

    except APIConnectionError as error:
        raise RuntimeError("Could not connect to the OpenAI API.") from error

    except APIStatusError as error:
        raise RuntimeError(
            f"OpenAI API returned status {error.status_code}."
        ) from error


def get_embedding(text: str) -> list[float]:
    """
    Generate an embedding for a single text.

    Args:
        text: Non-empty input text.

    Returns:
        Embedding vector.
    """
    return get_embeddings([text])[0]
