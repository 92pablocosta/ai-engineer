cpf = "09575980417"

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
    print('This CPF is VALID.')
else:
    print('Invalid CPF.')
