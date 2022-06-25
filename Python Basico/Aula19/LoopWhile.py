"""
Utilizado para realizar acoes enquanto uma condicao for verdadeira
"""

# while True:
    # nome = input("Qual seu nome: ")
    # print(f'Ola {nome}')

# print('Nao sera executado')

teste = 0
while teste < 10:
    if teste == 3:
        teste += 1
        continue  # pula o 3

    print(teste)
    teste += 1

x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'({x},{y})')
        y += 1

    x += 1

while True:
    print()
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ao: ')

    if sair.lower() == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Favor usar apenas caracteres validos (numeros)')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador invalido.')
