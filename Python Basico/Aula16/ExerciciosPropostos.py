"""
Faca um programa que peca ao usuario para digitar um numero inteiro,
informe se este numero e par ou impar. Caso o usuario nao digite um numero
inteiro, informe que nao e um numero inteiro.
"""

numero_inteiro = input('Digite um numero inteiro: ')

if numero_inteiro.isnumeric():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
        print('Par')
    else:
        print('Impar')
else:
    print('Nao e um numero inteiro.')

"""
Faca um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudacao apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input('Que horas sao (0 - 23): ')

if horas.isnumeric():
    horas = int(horas)

    if not horas > 23:
        if horas <= 11:
            print('Bom dia')
        elif horas <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
    else:
        print('Por favor digite um horario valido (0 - 23)')
else:
    print('Digite um numero valido (0 - 23)')

"""
Faca um programa que peca o primeiro nome do usuario. Se o nome tiver 4 letras ou
menos escreva "Seu nome e curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome e normal"; maior que 6 escreva "Seu nome e muito grande".
"""

nome = input('Nome: ')

tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome e curto')
elif tamanho_nome <= 6:
    print('Seu nome e normal')
else:
    print('Seu nome e muito grande')
