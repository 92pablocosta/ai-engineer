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

def add(expression: list) -> float:
    n1 = float(expression[0])
    n2 = float(expression[2])

    return n1 + n2

def subtract(expression: list) -> float:
    n1 = float(expression[0])
    n2 = float(expression[2])

    return n1 - n2

def multiply(expression: list) -> float:
    n1 = float(expression[0])
    n2 = float(expression[2])

    return n1 * n2

def divide(expression: list) -> float:
    n1 = float(expression[0])
    n2 = float(expression[2])

    try:
        result = n1 / n2
    except ZeroDivisionError:
        return 'Cannot divide by 0.'
    else:
        return result
