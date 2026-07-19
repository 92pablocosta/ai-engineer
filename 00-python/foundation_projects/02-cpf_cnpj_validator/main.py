from functions import identify_input

while True:
    number = str(input("Type a CPF or CNPJ [type 0 to exit]: "))
    if number.strip() == '0':
        break

    validation_result = identify_input(number)
    print(validation_result[1])
