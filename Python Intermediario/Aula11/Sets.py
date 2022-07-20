"""
Nao respeita ordem iteracao de uma string
Nao aceita 2 itens iguais
Add (adiciona), update (atualiza), clear, discard
uniao | une
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (elementos que estao nos dois sets, mas nao em ambos)
"""

set1 = {1,2,3,4,5}

print(set1)

for v in set1:
    print(v)


set1 = set()
set1.add(1)
set1.add(2)
set1.discard(2)

print(set1)


set1 = set()
set1.update('Python')

print(set1)


set1 = set()
set1.update([1,2,3,4,5], {5,6,7,8})

print(set1)


# serve principalmente para remover itens duplicados de listas
lista = [1,2,1,2,1,2,1,2,3,4,5,6,6,6,6,6,6,6,7,8,9,'Paulo','Paulo']
lista = set(lista)
lista = list(lista)

print(lista)


set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5,6}

set3 = set1 | set2

print(set3)

set3 = set1 & set2

print(set3)

set3 = set2 - set1

print(set3)

set3 = set1 ^ set2

print(set3)


lista = ['Paulo', 'Henrique', 'Joao']
lista2 = ['Paulo', 'Paulo', 'Henrique', 'Joao', 'Joao']

lista = list(set(lista))
lista2 = list(set(lista2))

print(lista, lista2)

