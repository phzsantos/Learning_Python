l1 = [1,2,3,4,5,6]
l2 = [v*2 for v in l1]
print(l2)


lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x: y for x, y in lista}  # ou d1 = dict(lista)
print(d1)


lista = [
    ('chave', 2),
    ('chave2', 'valor2'),
]

d1 = {x: y*2 for x, y in lista}
print(d1)


lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x.upper(): y.upper() for x, y in lista}
print(d1)


d1 = {x: y for x, y in enumerate(range(5))}
print(d1)


d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1)