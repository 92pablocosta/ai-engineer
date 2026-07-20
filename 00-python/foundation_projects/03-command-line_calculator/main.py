from functions import expression_isvalid
from functions import *

while True:
    expression = input("type an expression: ").strip().split()
    print("Type 0 to leave.")

    if expression == '0':
        break
    if expression_isvalid(expression):


print('Closing application.')
