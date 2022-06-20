nome = 'Paulo'
idade =  20
altura = 1.75
e_maior = idade > 18
peso = 80
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc e', imc)
print(f'{nome} tem {idade} anos de idade e seu imc e {imc:.2f}')
print('{} tem {} anos de idade e seu imc e {:.2f}'.format(nome, idade, imc))
