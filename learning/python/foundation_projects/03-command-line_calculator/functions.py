def expression_isvalid(exp: list) -> bool:
    valid_operators = ['+', '-', '*', '/']

    if len(exp) < 3 or len(exp) % 2 == 0:
        return False
    
    for index, part in enumerate(exp):
        if index % 2 == 0:
            try:
                float(part)
            except ValueError:
                return False
        else:
            if part not in valid_operators:
                return False
    
    return True

def calculate_expression(exp: str) -> float:
    result = float(exp[0])
    for index, value in enumerate(exp):
        if value == '+':
            result = result + float(exp[index + 1])
        elif value == '-':
            result = result - float(exp[index + 1])
        elif value == '*':
            result = result * float(exp[index + 1])
        elif value == '/':
            try:
                result = result / float(exp[index + 1])
            except ZeroDivisionError:
                return 'Division by "0" is not allowed.'
    return result
