# Relatório de Aprendizado — Login System com `.txt`

**Data:** 25 de agosto de 2026  
**Projeto:** Login System with File Persistence

## Objetivo da sessão

Construir um sistema de cadastro e login em Python, salvando os usuários em um arquivo `.txt` para que os dados permaneçam disponíveis após o encerramento do programa.

## Funcionalidades implementadas

- Cadastro de username e password.
- Persistência dos dados em `users.txt`.
- Leitura dos usuários salvos.
- Rejeição de usernames duplicados.
- Rejeição de campos vazios.
- Autenticação por username e password.
- Listagem apenas dos usernames, sem exibir passwords.
- Criação de `users.txt` na primeira execução.
- Menu contínuo com opção de saída.
- Limite de três tentativas de login durante a sessão.

## Conceitos de Python praticados

### Funções

O programa foi separado em funções com responsabilidades específicas, como salvar, carregar, cadastrar, autenticar e listar usuários.

### Entrada de dados

Foi utilizado `input()` para receber dados do usuário. Também foi aprendido que `input()` sempre retorna uma string e que `.strip()` deve ser aplicado ao valor retornado:

```python
username = input("Enter your username: ").strip()
```

### Condicionais

Foram usados `if`, `elif` e `else` para controlar o menu, validar campos e verificar as credenciais.

### Laços

- `while True` manteve o menu em execução.
- `break` encerrou o menu.
- `for line in file` percorreu o arquivo linha por linha.
- `continue` ignorou linhas vazias.

### Dicionários

Os usuários carregados do arquivo foram representados como pares de chave e valor:

```python
{
    "alice": "123",
    "bob": "456"
}
```

Foi praticado que:

- `username in users` procura uma chave.
- `users[username]` acessa o valor associado àquela chave.
- Percorrer `users` com `for` percorre suas chaves.

### Manipulação de arquivos

Foi utilizado `with open(...) as file` para garantir que o arquivo seja fechado automaticamente.

- Modo `"r"`: leitura.
- Modo `"a"`: adição ao final e criação do arquivo quando necessário.
- Modo `"w"`: criação ou sobrescrita do arquivo.

Cada usuário foi armazenado em uma linha no formato:

```text
username:password
```

### Tratamento de erros

Foi usado `try/except FileNotFoundError` para tratar a primeira execução, quando `users.txt` ainda não existe.

### Strings e desempacotamento

A instrução abaixo separou cada linha apenas no primeiro `:` e guardou as partes em duas variáveis:

```python
username, password = line.split(":", 1)
```

Também foi estudado o caractere `\n`, usado para representar uma quebra de linha.

### Valores booleanos e retornos

A função de login passou a retornar `True` no sucesso e `False` na falha. Isso permitiu que o programa principal atualizasse o contador de tentativas.

### Avaliação de curto-circuito

Na condição:

```python
username in users and users[username] == password
```

o Python só acessa `users[username]` quando o username existe, evitando um `KeyError`.

## Erros encontrados e aprendizados

- `print()` não deve ser colocado dentro de `input()` para formar o prompt.
- A indentação de `return` determina se ele pertence ou não a um `if`.
- Colocar o contador dentro do `while` fazia seu valor voltar a zero a cada repetição.
- Chamar `login_user()` duas vezes solicitava as credenciais duas vezes.
- Retornar uma tupla como `(True, message)` não exibe automaticamente a mensagem.
- `.strip()` deve ser aplicado ao resultado de `input()`, não ao texto do prompt.

## Limitações da versão atual

- As passwords são armazenadas como texto simples. Isso é aceitável somente para este exercício; sistemas reais devem armazenar hashes seguros.
- O limite de tentativas é global para a sessão, não separado por username.
- Um login bem-sucedido não reinicia o contador de falhas.
- O formato baseado em `:` exige cuidado quando os dados contêm caracteres especiais ou quebras de linha.

## Próximo passo

Refazer o exercício usando JSON. A próxima versão deve comparar:

- `json.load()` com a leitura manual de linhas.
- `json.dump()` com a escrita manual usando `file.write()`.
- Representação direta de dicionários em JSON.
- Tratamento de arquivo inexistente e JSON vazio ou inválido.

