"""
Iniciar com letra, pode conter numeros, separar _, letras minusculas sao diferentes de maiusculas
"""

nome = 'Paulo'
idade =  20
altura = 1.75
e_maior = idade > 18
peso = 80

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('E maior:', e_maior)

imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc e', imc)
