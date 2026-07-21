# Python OOP — Exercícios de Fundamentos

Estes exercícios treinam os conceitos estudados até agora: classes, objetos, atributos, métodos, `__init__`, `self`, valores padrão, `__str__`, regras de negócio e `@property`.

Não consulte soluções antes de tentar. Crie um arquivo `.py` separado para cada exercício e faça testes próprios ao final.

---

## Exercício 1 — Classe `Student`

Crie uma classe `Student` para representar um aluno.

### Requisitos

- Atributos de instância: `name` e `age`.
- Método `introduce()` que exibe uma apresentação do aluno.
- Método `have_birthday()` que aumenta a idade em 1.
- Método especial `__str__()` que retorna uma representação amigável do objeto.

### Testes mínimos

- Crie dois alunos diferentes.
- Exiba os dois objetos com `print()`.
- Chame `introduce()` para cada aluno.
- Faça aniversário de um deles e confirme que a idade mudou.

---

## Exercício 2 — Classe `BankAccount`

Crie uma classe `BankAccount` para representar uma conta bancária simples.

### Requisitos

- Atributos de instância: `owner`, `account_number` e `balance`.
- Método `deposit(amount)` que adiciona um valor ao saldo.
- Método `withdraw(amount)` que retira um valor apenas se houver saldo suficiente.
- Caso o saque não possa ser realizado, mostre uma mensagem clara e não altere o saldo.
- Método especial `__str__()` que mostra o titular, o número da conta e o saldo formatado com duas casas decimais.

### Testes mínimos

- Crie uma conta com saldo inicial.
- Faça um depósito.
- Faça um saque válido.
- Tente sacar um valor maior que o saldo disponível.
- Confira o estado final da conta com `print()`.

---

## Exercício 3 — Classe `Book`

Crie uma classe `Book` para representar um livro de biblioteca.

### Requisitos

- Atributos de instância: `title`, `author`, `pages` e `is_borrowed`.
- `is_borrowed` deve começar com o valor `False`.
- Método `borrow()` que marca o livro como emprestado.
- Método `return_book()` que marca o livro como disponível novamente.
- Método `show_status()` que informa se o livro está disponível ou emprestado.
- Método especial `__str__()` que apresenta pelo menos título e autor.
- Não permita emprestar novamente um livro que já esteja emprestado; mostre uma mensagem apropriada.

### Testes mínimos

- Crie um livro.
- Mostre o status inicial.
- Empreste o livro e mostre o novo status.
- Tente emprestá-lo uma segunda vez.
- Devolva o livro e confirme que ele voltou a ficar disponível.

---

## Exercício 4 — Classe `Car`

Crie uma nova versão da classe `Car` para praticar estado interno e propriedades.

### Requisitos

- Atributos de instância: `brand`, `model`, `year` e `_speed`.
- `_speed` deve iniciar em `0`.
- Crie uma propriedade somente leitura chamada `speed` usando `@property`.
- Método `accelerate(amount=10)` que aumenta a velocidade, sem ultrapassar `180`.
- Método `brake(amount=10)` que reduz a velocidade, sem ficar abaixo de `0`.
- Método `stop()` que define a velocidade como `0`.
- Método especial `__str__()` que exibe os dados do carro e a velocidade atual.

### Testes mínimos

- Crie um carro e confira sua velocidade inicial.
- Acelere com o valor padrão e com um valor informado.
- Tente ultrapassar `180 km/h`.
- Freie com o valor padrão e com um valor informado.
- Tente reduzir a velocidade para abaixo de `0`.
- Pare o carro usando `stop()`.

---

## Exercício 5 — Classe `ShoppingCart`

Crie uma classe `ShoppingCart` para representar um carrinho de compras.

### Requisitos

- Atributos de instância: `customer_name` e `items`.
- `items` deve começar como uma lista vazia.
- Método `add_item(product, price)` que adiciona um item ao carrinho.
- Cada item deve ser armazenado como um dicionário neste formato:

  ```python
  {"product": "Keyboard", "price": 150.00}
  ```

- Método `show_items()` que exibe os produtos e seus preços.
- Método `calculate_total()` que retorna a soma dos preços dos itens.
- Método `clear_cart()` que remove todos os itens do carrinho.
- Método especial `__str__()` que mostra o nome do cliente e a quantidade de itens.

### Testes mínimos

- Crie um carrinho para um cliente.
- Adicione três produtos.
- Liste os itens inseridos.
- Calcule e exiba o total da compra.
- Exiba o objeto com `print()`.
- Limpe o carrinho e confirme que não há mais itens.

---

## Critérios de revisão

Antes de considerar cada exercício concluído, confirme:

- A classe possui um nome claro em `PascalCase`.
- Os atributos são criados dentro de `__init__` usando `self`.
- Os métodos têm nomes em `snake_case` e responsabilidades claras.
- Cada método altera apenas o estado necessário.
- Os casos inválidos preservam o estado do objeto.
- Os testes cobrem o fluxo normal e pelo menos um caso de limite ou erro.
