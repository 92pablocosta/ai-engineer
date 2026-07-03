import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

chunks = [
    "Embeddings transformam texto em vetores numéricos que capturam significado, permitindo busca semântica em vez de busca por palavra exata.",
    "RAG combina recuperação de documentos com geração de texto: o modelo busca trechos relevantes antes de responder.",
    "Reranking usa um modelo cross-encoder para reordenar os resultados recuperados, melhorando a precisão do topo da lista.",
    "Hybrid retrieval combina busca densa por embeddings com busca esparsa por palavras-chave como o BM25.",
    "Docker empacota uma aplicação e suas dependências em um container isolado que roda igual em qualquer máquina.",
    "PostgreSQL é um banco de dados relacional, e a extensão pgvector permite armazenar e buscar embeddings dentro dele.",
    "A pentatônica menor é a primeira escala que a maioria dos guitarristas aprende para improvisar solos de blues e rock.",
    "Trocar as cordas de um violão regularmente mantém o brilho do som e evita que oxidem e percam afinação.",
    "O método de coar café V60 produz uma bebida mais limpa e ácida, valorizando notas mais delicadas do grão.",
    "Massa de pizza napolitana leva poucos ingredientes, mas precisa de longa fermentação para desenvolver sabor e textura.",
    "João Pessoa é a capital da Paraíba e abriga a Ponta do Seixas, o ponto mais a leste das Américas.",
    "A Austrália é o único país que ocupa um continente inteiro, com a maior parte do território coberta por deserto.",
    "O agachamento livre trabalha quadríceps, glúteos e core, e é considerado um dos exercícios mais completos de membros inferiores.",
    "A progressão de carga é o princípio de aumentar gradualmente o peso ou as repetições para forçar o músculo a se adaptar.",
    "Fotossíntese é o processo pelo qual plantas convertem luz solar, água e gás carbônico em glicose e oxigênio.",
    "O Sol é uma estrela de tamanho médio e responde por mais de 99% de toda a massa do sistema solar.",
    "Juros compostos fazem o dinheiro render sobre o próprio rendimento acumulado, crescendo de forma exponencial no tempo.",
    "A Muralha da China tem milhares de quilômetros e foi construída ao longo de séculos por diferentes dinastias.",
    "O ciclo da água envolve evaporação, condensação e precipitação, movendo a água continuamente entre oceano, atmosfera e solo.",
    "Abelhas polinizam grande parte das plantas que produzem os alimentos que consumimos diariamente.",
]


def embed(texts: list[str]) -> np.ndarray:
    """
    Manda uma lista de textos pra API, devolve uma matriz (n_textos, 1536).
    """
    
    resp = client.embeddings.create(model="text-embedding-3-small", input=texts)
    return np.array([d.embedding for d in resp.data])


# embeda os chunks UMA vez só (não a cada query — isso custa tempo e dinheiro)
chunk_vectors = embed(chunks)  # shape: (20, 1536)


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def retrieve(query, k=1):
    query_vector = embed([query])[0]

    scores = [cosine_similarity(query_vector, vec) for vec in chunk_vectors]

    top_indices = np.argsort(scores)[::-1][:k]

    return [chunks[i] for i in top_indices]


for q in [
    "como funciona busca por significado?",
    "qual escala aprender pra improvisar?",
    "diferença entre busca densa e por palavra-chave",
]:
    print(f"\nQUERY: {q}")
    for hit in retrieve(q):
        print(" -", hit)
