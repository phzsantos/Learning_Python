"""
count - itertools
"""
from itertools import count

contador = count(start=-1, step=-1)

for valor in contador:
    print(round(valor, 2))

    if valor >= 10 or valor <= -10:
        break


contador = count()
lista = ['Paulo', 'Henrique', 'Guerra', 'Jose', 'Eduardo']
lista = zip(contador, lista)

print(list(lista))