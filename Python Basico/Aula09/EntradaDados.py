nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")

ano_nascimento = 2022 - int(idade)

print(f'{nome} tem {idade} anos. {nome} nasceu em {ano_nascimento}.')

print(f'O usuario digitou {nome} e o tipo e {type(nome)}')

numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite outro numero: '))

print(numero_1 ** numero_2)
