"""
:s - Strings
:d - Inteiros
:f - Float
:. - Quantidade de casas decimais Float
: (Caractere) (>, < ou ^) (Quantidade) (tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3

divisao = num_1 / num_2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = 'Paulo Henrique'

print(f'{nome:s}')

numero = 1

print(f'{numero:0>10}')

numero2 = 1150

print(f'{numero2:0^10}')
print(f'{numero2:0>10.2f}')

print(f'{nome:#^50}')

nome_formatado = '{:@^26}'.format(nome)

print(nome_formatado)

print(nome.lower())  #tudo minusculo
print(nome.upper())  # tudo maiusculo
print(nome.title())  # Primeiras letras maiusculas
