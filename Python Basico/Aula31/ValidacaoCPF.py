"""
CPF = 168.995.350-09
=============================================
1 * 10 = 10          #      1 * 11 = 11
6 * 9  = 54          #      6 * 10 = 60
8 * 8  = 64          #      8 * 9  = 72
9 * 7  = 63          #      9 * 8  = 72
9 * 6  = 54          #      9 * 7  = 63
5 * 5  = 25          #      5 * 6  = 30
3 * 4  = 12          #      3 * 5  = 15
5 * 3  = 15          #      5 * 4  = 20
0 * 2  = 0           #      0 * 3  = 0
                     #      0 * 2  = 0
         297         #             343
11 - (297 % 11) = 11 #  11 - (343 % 11) = 9
11 > 9 = 0           #
Digito 1 = 0         #  Digito 2 = 9
"""

cpf = '16899535009'

soma = 0
contador = 10
for valor in cpf[:10]:
    numero = int(valor)
    soma += numero * contador
    contador -= 1

digito_1 = 11 - (soma % 11)

if digito_1 > 9:
    digito_1 = 0

soma = 0
contador = 11
for valor in cpf[:10]:
    numero = int(valor)
    soma += numero * contador
    contador -= 1
else:
    soma += digito_1 * contador

digito_2 = 11 - (soma % 11)

novo_cpf = cpf[:-2] + str(digito_1) + str(digito_2)

if cpf == novo_cpf:
    print('Valido')
else:
    print('Invalido')


cpf = '16899535009'
novo_cpf = cpf[:-2]

reverso = 10
total = 0
for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11

        digito_1 = 11 - (total % 11)

        if digito_1 > 9:
            digito_1 = 0
        total = 0
        novo_cpf += str(digito_1)

if cpf == novo_cpf:
    print('Valido')
else:
    print('Invalido')
