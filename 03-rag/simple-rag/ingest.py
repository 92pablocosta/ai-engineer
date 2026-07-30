import json
from pathlib import Path
from typing import TypedDict

import faiss
import numpy as np

from embeddings import get_embeddings

DATA_DIRECTORY = Path("data")
STORAGE_DIRECTORY = Path("storage")

INDEX_PATH = STORAGE_DIRECTORY / "index.faiss"
METADATA_PATH = STORAGE_DIRECTORY / "metadata.json"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
EMBEDDING_BATCH_SIZE = 100


class ChunkMetadata(TypedDict):
    source: str
    chunk_id: int
    content: str


def read_text_files(directory: Path) -> list[tuple[Path, str]]:
    """
    Read all TXT files from a directory.

    Args:
        directory: Directory containing the documents.

    Returns:
        List of tuples containing file paths and their contents.

    Raises:
        FileNotFoundError: If the directory does not exist.
        ValueError: If no valid TXT files are found.
    """
    if not directory.exists():
        raise FileNotFoundError(f"Data directory does not exist: {directory.resolve()}")

    documents: list[tuple[Path, str]] = []

    for file_path in sorted(directory.glob("*.txt")):
        try:
            content = file_path.read_text(encoding="utf-8").strip()
        except UnicodeDecodeError as error:
            raise ValueError(f"Could not decode file as UTF-8: {file_path}") from error
        except OSError as error:
            raise RuntimeError(f"Could not read file: {file_path}") from error

        if content:
            documents.append((file_path, content))

    if not documents:
        raise ValueError(f"No non-empty TXT files found in {directory.resolve()}.")

    return documents


def split_text(
    text: str,
    chunk_size: int = CHUNK_SIZE,
    chunk_overlap: int = CHUNK_OVERLAP,
) -> list[str]:
    """
    Split text into overlapping character-based chunks.

    Args:
        text: Text to split.
        chunk_size: Maximum number of characters per chunk.
        chunk_overlap: Number of characters shared between chunks.

    Returns:
        List of text chunks.

    Raises:
        ValueError: If the chunk configuration is invalid.
    """
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")

    if chunk_overlap < 0:
        raise ValueError("Chunk overlap cannot be negative.")

    if chunk_overlap >= chunk_size:
        raise ValueError("Chunk overlap must be smaller than chunk size.")

    normalized_text = " ".join(text.split())

    if not normalized_text:
        return []

    chunks: list[str] = []
    start = 0

    while start < len(normalized_text):
        end = min(start + chunk_size, len(normalized_text))
        chunk = normalized_text[start:end]

        if end < len(normalized_text):
            last_space = chunk.rfind(" ")

            if last_space > chunk_size // 2:
                end = start + last_space
                chunk = normalized_text[start:end]

        chunk = chunk.strip()

        if chunk:
            chunks.append(chunk)

        if end >= len(normalized_text):
            break

        start = end - chunk_overlap

    return chunks


def create_chunks(
    documents: list[tuple[Path, str]],
) -> list[ChunkMetadata]:
    """
    Split documents and create metadata for each chunk.

    Args:
        documents: Documents containing their file paths and contents.

    Returns:
        Metadata for all generated chunks.
    """
    chunks: list[ChunkMetadata] = []

    for file_path, content in documents:
        document_chunks = split_text(content)

        for chunk_id, chunk_content in enumerate(document_chunks):
            chunks.append(
                {
                    "source": file_path.name,
                    "chunk_id": chunk_id,
                    "content": chunk_content,
                }
            )

    if not chunks:
        raise ValueError("No chunks were generated.")

    return chunks


def generate_embeddings_in_batches(
    texts: list[str],
    batch_size: int = EMBEDDING_BATCH_SIZE,
) -> np.ndarray:
    """
    Generate embeddings in batches and convert them to a NumPy array.

    Args:
        texts: Texts to embed.
        batch_size: Number of texts sent per API request.

    Returns:
        Two-dimensional float32 NumPy array.
    """
    if batch_size <= 0:
        raise ValueError("Batch size must be greater than zero.")

    all_embeddings: list[list[float]] = []

    for start in range(0, len(texts), batch_size):
        batch = texts[start : start + batch_size]

        print(
            f"Generating embeddings "
            f"{start + 1}-{start + len(batch)} "
            f"of {len(texts)}..."
        )

        batch_embeddings = get_embeddings(batch)
        all_embeddings.extend(batch_embeddings)

    embeddings_array = np.asarray(
        all_embeddings,
        dtype=np.float32,
    )

    if embeddings_array.ndim != 2:
        raise ValueError("Embeddings must form a two-dimensional array.")

    return embeddings_array


def create_faiss_index(
    embeddings: np.ndarray,
) -> faiss.IndexFlatIP:
    """
    Create a FAISS cosine-similarity index.

    Args:
        embeddings: Two-dimensional float32 embedding matrix.

    Returns:
        FAISS index containing the normalized embeddings.
    """
    normalized_embeddings = embeddings.copy()

    faiss.normalize_L2(normalized_embeddings)

    embedding_dimension = normalized_embeddings.shape[1]

    index = faiss.IndexFlatIP(embedding_dimension)
    index.add(normalized_embeddings)

    return index


def save_index(
    index: faiss.Index,
    chunks: list[ChunkMetadata],
) -> None:
    """
    Save the FAISS index and chunk metadata.

    Args:
        index: Populated FAISS index.
        chunks: Metadata associated with index positions.
    """
    STORAGE_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    try:
        faiss.write_index(
            index,
            str(INDEX_PATH),
        )

        METADATA_PATH.write_text(
            json.dumps(
                chunks,
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

    except OSError as error:
        raise RuntimeError("Could not save the index files.") from error


def ingest_documents() -> None:
    """
    Run the complete document ingestion pipeline.
    """
    print("Reading documents...")
    documents = read_text_files(DATA_DIRECTORY)

    print(f"Documents found: {len(documents)}")

    print("Creating chunks...")
    chunks = create_chunks(documents)

    print(f"Chunks created: {len(chunks)}")

    texts = [chunk["content"] for chunk in chunks]

    embeddings = generate_embeddings_in_batches(texts)

    print(f"Embedding dimensions: {embeddings.shape[1]}")

    print("Creating FAISS index...")
    index = create_faiss_index(embeddings)

    if index.ntotal != len(chunks):
        raise RuntimeError("FAISS index size does not match metadata size.")

    print("Saving index and metadata...")
    save_index(index, chunks)

    print(f"Indexed vectors: {index.ntotal}")
    print(f"FAISS index saved to: {INDEX_PATH}")
    print(f"Metadata saved to: {METADATA_PATH}")


if __name__ == "__main__":
    try:
        ingest_documents()
    except Exception as error:
        print(f"Ingestion failed: {error}")
        raise SystemExit(1) from error
