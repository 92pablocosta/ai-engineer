def identifyInput(number: str):
    number = number.replace(".", "").replace("/", "").replace("-", "")

    if not number.isnumeric():
        return False, 'CPF or CNPJ must be numbers only.'
    
    if len(number) == 11:
        return validateCPF(number)
    elif len(number) == 14:
        return validateCNPJ(number)
    else:
        return False, 'Invalid CPF or CNPJ'



def validateCPF(cpf: str):
    add = 0

    for i in range(9):
        add += int(cpf[i]) * (10 - i)

    rest = add % 11

    if rest < 2:
        first_digit = 0
    else:
        first_digit = 11 - rest

    add = 0
    for i in range(10):
        if (11 - i) == 2:
            add += first_digit * 2
        else:
            add += int(cpf[i]) * (11 - i)

    rest = add % 11

    if rest < 2:
        second_digit = 0
    else:
        second_digit = 11 - rest

    if int(cpf[-2]) == first_digit and int(cpf[-1]) == second_digit:
        return True, 'CPF Validated.'
    else:
        return False, 'CPF number is not valid.'
    

def validateCNPJ(cnpj: str):
    soma = 0

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    for i in range(12):
        soma += int(cnpj[i]) * pesos1[i]
    resto = soma % 11
    primeiro_digito = 0 if resto < 2 else 11 - resto

    cnpj_base_13 = cnpj[:12] + str(primeiro_digito)

    soma = 0

    for i in range(13):
        soma += int(cnpj_base_13[i]) * pesos2[i]
    resto = soma % 11
    if resto < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - resto

    if int(cnpj[-2]) == primeiro_digito and int(cnpj[-1]) == segundo_digito:
        return True, "CNPJ validated"
    else:
        return False, "Invalid CNPJ"

