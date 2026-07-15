def checkCpfDigit(cpf: str):
    add = 0
    first_digit = 0
    second_digit = 0

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
        return True
    else:
        return False


def validateCPF(cpf: str):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11:
        return False, 'Invalid CPF'
    if cpf.isdigit():
        return True, 'CPF Válido'
    else:
        return False, 'CPF inválido'


def validateCNPJ(cnpj: str):
    pass
