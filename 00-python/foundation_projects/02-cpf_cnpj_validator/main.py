from functions import identifyInput

cpf_cnpj = str(input("Type a CPF or CNPJ: ")).strip()

print(identifyInput(cpf_cnpj))
