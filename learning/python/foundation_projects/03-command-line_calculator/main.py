from functions import *
from rich import print

while True:
    exp = input('Type an expression or "0" to leave: ').strip().split()

    if exp[0] == '0':
        break

    if expression_isvalid(exp):
        result = calculate_expression(exp)
        print(f'Result: {result}')
    else:
        print('[red bold]Not a valid expression, please try again.[/red bold]')

print('[blue]Program closed.[blue]')
