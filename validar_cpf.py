cpf = input('Digite o cpf: ')
cpf_new = cpf[:-2]
cnt_1 = 10
cnt_2 = 11
soma_1 = soma_2 = 0

for c in cpf_new:
    c = int(c)
    resultado = c * cnt_1
    cnt_1 -= 1
    soma_1 += resultado

digito_1 = 11 - (soma_1 % 11)

if digito_1 > 9:
    digito_1 = '0'
    cpf_new += digito_1
else:
    digito_1 = str(digito_1)
    cpf_new += digito_1

for c in cpf_new:
    c = int(c)
    result = c * cnt_2
    cnt_2 -= 1
    soma_2 += result
digito_2 = 11 - (soma_2 % 11)

if digito_2 > 9:
    digito_2 = '0'
    cpf_new += digito_2
else:
    digito_2 = str(digito_2)
    cpf_new += digito_2

if cpf_new == cpf:
    print(f'O CPF: {cpf_new} é válido.')
else:
    print(f'O CPF: {cpf_new} é invalido')
