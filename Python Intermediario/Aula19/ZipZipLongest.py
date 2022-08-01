"""
Zip - unindo iteraveis
Zip longest - Itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['Sao Paulo','Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(
    indice, 
    estados, 
    cidades
)

for valor in cidades_estados:
    print(valor)


cidades_estados = zip_longest(
    estados, 
    cidades, 
    fillvalue='Estado'
)

print()
for valor in cidades_estados:
    print(valor)
