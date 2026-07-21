exp = "10 - 4 + 2".split()

def expression_isvalid(exp: list) -> tuple[bool, str]:
    valid_operators = ['+', '-', '*', '/']

    if len(exp) < 3 or len(exp) % 2 == 0:
        return False, 'Invalid expression.'
    
    for index, part in enumerate(exp):
        if index % 2 == 0:
            try:
                float(part)
            except ValueError:
                return False, f'"{part}" is not a valid number.'
        else:
            if part not in valid_operators:
                return False, f'"{part}" is not a valid operator.'
    
    return True, ''

print(expression_isvalid("10 + 5".split()))
print(expression_isvalid("10 + 5 - 3".split()))
print(expression_isvalid("10 % 5".split()))
print(expression_isvalid("10 + five".split()))
print(expression_isvalid("10 +".split()))
print(expression_isvalid("10 5".split()))
