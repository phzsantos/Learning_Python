"""
Split, join, Enumerate em python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumarete - Enumerar elementos da lista # iteraveis
"""

string = 'O Brasil e o pais do futebol, o Brasil e penta.'

lista = string.split(' ')
lista2 = string.split(',')

print(lista)
print(lista2)

for valor in lista:
    print(valor)

for valor in lista:
    print(f'A palavra {valor} apareceu {lista.count(valor)}x na frase')

palavra = ''
contagem = 0
for valor in lista:
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes e "{palavra}" {contagem}x')

for valor in lista2:
    print(valor)

for valor in lista2:
    print(valor.strip().capitalize())


string = 'O Brasil e penta'
lista = string.split(' ')
string2 = ' '.join(lista)

print(string)
print(lista)
print(string2)


string = 'O brasil e penta'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor)

lista = [
    [0, 1],
    [2, 3],
    [4, 5],
]

for v in lista:
    print(v[0], v[1])

lista = [
    [0, 'Paulo'],
    [1, 'Henrique'],
    [2, 'Teste'],
]

for indice, nome in lista:
    print(indice, nome)

lista = ['Paulo', 'Henrique', 'Teste']

for indice, nome in enumerate(lista):
    print(indice, nome)

n1, n2, n3 = lista

print(n1, n2, n3)
