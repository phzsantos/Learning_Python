"""
== > >= < <= !=
"""

num1 = 2
num2 = 2

expressao = num1 != num2

print(expressao)

var1 = 'Paulo'
var2 = 'Secreto'

expressao = var1 != var2

print(expressao)

nome = input('Qual o seu nome: ')
idade = int(input('Qual a sua idade: '))

menor_idade = 20
maior_idade = 30

if idade >= menor_idade and idade <= maior_idade:
    print(f'{nome} pode pegar o imprestimo.')
else:
    print(f'{nome} NAO pode pegar o imprestimo.')
