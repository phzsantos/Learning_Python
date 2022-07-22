l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]
print(l2)


l3 = [v * 2 for v in l1]
print(l3)


l4 = [(v, v2) for v in l1 for v2 in range(3)]
print(l4)


l5 = ['Paulo', 'Henrique', 'Santos']
l5 = [v.replace('a', '@').upper() for v in l5]
print(l5)


tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
l6 = [(y, x) for x, y in tupla]
print(l6)


l7 = list(range(100))
ex6 = [v for v in l7 if v % 3 == 0 if v % 8 == 0]
print(ex6)


ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l7]
print(ex7)
