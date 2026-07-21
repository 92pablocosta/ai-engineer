def identify_input(number: str):
    try:
        number = number.strip().replace(".", "").replace("/", "").replace("-", "")
    except (TypeError, AttributeError):
        return False, 'Input must be a string or convertible to a string.'
    else:
        if not number.isdecimal():
            return False, 'CPF or CNPJ must be numbers only.'

        if number == number[0] * len(number):
            return False, "CPF or CNPJ cannot be a sequence of repeated digits."
        
        if len(number) == 11:
            return validate_cpf(number)
        elif len(number) == 14:
            return validate_cnpj(number)
        else:
            return False, 'Invalid CPF or CNPJ'



def validate_cpf(cpf: str):
    total = 0

    for i in range(9):
        total += int(cpf[i]) * (10 - i)

    remainder = total % 11

    if remainder < 2:
        first_digit = 0
    else:
        first_digit = 11 - remainder

    total = 0
    for i in range(10):
        if (11 - i) == 2:
            total += first_digit * 2
        else:
            total += int(cpf[i]) * (11 - i)

    remainder = total % 11

    if remainder < 2:
        second_digit = 0
    else:
        second_digit = 11 - remainder

    if int(cpf[-2]) == first_digit and int(cpf[-1]) == second_digit:
        return True, 'CPF Validated.'
    else:
        return False, 'CPF number is not valid.'
    

def validate_cnpj(cnpj: str):
    total = 0

    first_weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    second_weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    for i in range(12):
        total += int(cnpj[i]) * first_weights[i]
    remainder = total % 11
    first_digit = 0 if remainder < 2 else 11 - remainder

    cnpj_with_first_digit = cnpj[:12] + str(first_digit)

    total = 0

    for i in range(13):
        total += int(cnpj_with_first_digit[i]) * second_weights[i]
    remainder = total % 11
    if remainder < 2:
        second_digit = 0
    else:
        second_digit = 11 - remainder

    if int(cnpj[-2]) == first_digit and int(cnpj[-1]) == second_digit:
        return True, "CNPJ validated"
    else:
        return False, "Invalid CNPJ"
