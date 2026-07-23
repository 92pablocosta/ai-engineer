import os
import json
import faiss
import numpy as np
from embeddings import get_embedding

DATA_DIR = "data"
INDEX_PATH = "index.faiss"
CHUNKS_PATH = "chunks.json"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

def read_files(data_dir: str) -> list[str]:
    texts = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            path = os.path.join(data_dir, filename)
            with open(path, "r", encoding="utf-8") as f:
                texts.append(f.read())
    return texts


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


def main():
    all_chunks = []
    for text in read_files(DATA_DIR):
        all_chunks.extend(chunk_text(text))

    print(f"Total de chuncks: {len(all_chunks)}")

    embeddings = [get_embedding(chunk) for chunk in all_chunks]
    dimension = len(embeddings[0])

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings, dtype="float32"))

    faiss.write_index(index, INDEX_PATH)

    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    print(f"Index saved in {INDEX_PATH}")
    print(f"Chunks saved in {CHUNKS_PATH}")

if __name__ == "__main__":
    main()
