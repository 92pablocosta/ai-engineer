# Progresso - Pytest

## Contexto

Pasta focada em aprender pytest do zero, com exercicios pequenos e revisao passo a passo.

## Aula 1 - Primeiro teste com pytest

Status: concluida.

### Objetivo

Entender como o pytest descobre testes, executa `assert` e mostra uma falha legivel quando o resultado esperado nao bate com o resultado real.

### Arquivos criados pelo aluno

- `project1/calculator.py`
- `project1/test_calculator.py`

### Codigo trabalhado

`project1/calculator.py` contem uma funcao simples de soma:

```python
def add(n1: int, n2: int) -> int:
    return n1 + n2
```

`project1/test_calculator.py` comecou com uma tentativa usando `return` dentro do teste. Isso foi corrigido conceitualmente: teste em pytest deve verificar comportamento com `assert`, nao retornar valores ou strings.

### Conceitos praticados

- Pytest descobre arquivos no formato `test_*.py`.
- Pytest descobre funcoes no formato `test_*`.
- Testes devem usar `assert`, nao `return`.
- `python -m pytest -q` executa os testes em modo resumido.
- Uma falha de assert mostra o valor esperado, o valor recebido e a linha do teste.
- Para testes pequenos, `assert add(2, 5) == 7` e suficiente.
- Para melhor leitura, tambem pode usar Arrange-Act-Assert:

```python
def test_add_two_numbers():
    result = add(2, 5)

    assert result == 7
```

### Saida quando passou

```text
.                                                           [100%]
1 passed in 0.00s
```

Leitura correta:

- O ponto (`.`) representa um teste que passou.
- `[100%]` indica que todos os testes coletados terminaram.
- `1 passed` confirma que havia um teste e ele passou.

### Exemplo de falha analisada

```text
assert add(2, 5) == 6
E       assert 7 == 6
E        +  where 7 = add(2, 5)
```

Leitura correta:

- A funcao `add(2, 5)` retornou `7`.
- O teste esperava `6`.
- O problema estava na expectativa do teste, nao na funcao.

Tambem foi analisado o resumo:

```text
FAILED test_calculator.py::test_add_two_numbers - assert 7 == 6
```

Leitura correta:

- O teste que falhou foi `test_add_two_numbers`.
- A falha aconteceu em `test_calculator.py`.
- O motivo resumido foi `assert 7 == 6`.

### Comandos usados

```bash
python -m pytest -q
```

### Observacao de ambiente

Inicialmente o pytest nao estava instalado no Python usado pelo terminal. O erro foi:

```text
No module named pytest
```

Depois de instalar/usar o ambiente correto, o teste executou normalmente.

## Proxima aula

Aula 2: testar excecoes com `pytest.raises`.

Objetivo:

- Criar uma funcao que pode falhar de forma esperada.
- Escrever um teste que confirma que a excecao correta foi levantada.
- Entender a diferenca entre bug inesperado e erro esperado do dominio.
