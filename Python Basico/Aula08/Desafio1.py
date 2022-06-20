"""
* Criar variaveis para nome (str), idade (int)
* altura (float) e peso (float) de uma pessoa
* Criar variavel com ano atual (int)
* obter ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obeter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-strings (com as chaves)
"""

nome = 'Paulo'
idade = 20
altura = 1.75
peso = 97.50
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} e {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}')
