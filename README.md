# AI Engineer — learning in public

Registro público da minha evolução para AI/Backend Engineer de produção. Este repositório é um diário de aprendizagem: cada exercício, teste e decisão deve comprovar entendimento real — não construir um portfólio de projetos prontos.

## Estrutura

```text
.
├── learning/    # exercícios de Python, pytest e FastAPI
├── docs/        # roadmap e documentação pública do percurso
└── archive/     # experimentos anteriores, fora do plano atual
```

Os exercícios ficam organizados por assunto, não como versões de um produto. Um projeto original só será definido quando os fundamentos necessários estiverem consolidados. Credenciais, ambientes virtuais, caches e dados locais ficam fora do Git conforme o [`.gitignore`](.gitignore).

## Progresso da fundação

| Fase | Foco |
| --- | --- |
| 0 | Python, OOP, tipos e async |
| 1 | pytest, fixtures e mocks |
| 2 | FastAPI, Pydantic e streaming |
| 3 | Embeddings, retrieval, pgvector e RAG |
| 4 | Evals, tracing e observabilidade |
| 5 | Docker, AWS e S3 |

Leia o [roadmap completo](docs/roadmap.md) antes de iniciar uma fase. Durante os exercícios de fundação, o código é escrito à mão; IA entra depois para revisão e desbloqueio.

## Desenvolvimento

Cada exercício documenta seus próprios comandos e dependências. Para o percurso atual de pytest:

```bash
cd learning/pytest
python3 -m pytest -q project1
```

Projetos futuros devem usar `uv`, Ruff, mypy e pytest desde o início.
