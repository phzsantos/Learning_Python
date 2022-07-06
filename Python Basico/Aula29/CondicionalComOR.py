nome = input('Qual seu nome: ')

if nome:
    print(nome)
else:
    print('Voce nao digitou nada.')


nome = input('Qual seu nome: ')

print(nome or 'Voce nao digitou nada')


a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g

print(variavel)
