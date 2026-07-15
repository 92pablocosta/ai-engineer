def validateCPF(cpf: str):
    cpf = cpf.replace(".", "").replace("-", "")
    if cpf.isdigit():
        return 'CPF Válido'
    else:
        return 'CPF inválido'
    

def validateCNPJ(cnpj: str):
    pass

