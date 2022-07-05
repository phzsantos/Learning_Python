lista = ['Luiz', 'Joao', 'Maria']

n1, n2, n3 = lista

print(n1, n2, n3)

lista2 = ['Luiz', 'Joao', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, *outra_lista, ultimo_da_lista = lista2

print(n1, n2, ultimo_da_lista)
print(outra_lista)

*outra_lista, n1, n2, n3 = lista2

print(n1, n2, n3)

n1, n2, *_ = lista2

print(n1, n2)
