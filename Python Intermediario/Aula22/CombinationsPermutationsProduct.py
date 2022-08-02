"""
Combinations, Permutations, e Produto - Itertools
Combinations - Ordem nao importa
Permutations - Ordem importa
Product - Ordem importa e repete valores unicos
"""
from itertools import combinations, permutations, product

pessoas = ['Paulo', 'Henrique', 'Bruno', 'Amanda', 'Maria', 'Socrates']

print('Combinations: ')
for grupo in combinations(pessoas, 2):
    print(grupo)

print('\nPermutations: ')
for grupo in permutations(pessoas, 2):
    print(grupo)

print('\nProduct: ')
for grupo in product(pessoas, repeat=2):
    print(grupo)