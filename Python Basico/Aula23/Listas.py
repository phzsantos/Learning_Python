"""
Listas em python:
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

#     +   0    1    2    3    4
lista = ['A', 'Bacana', 'C', 'D', 'E', 10.5]
#     -   5    4    3    2    1

string = 'ABCDE'

print(string[1])
print(lista[1])
print(lista[-1])
print(lista)

lista[5] = 'Qualquer outra coisa'

print(lista)
print(lista[:3])
print(lista[1:4])
print(lista[-1])
print(lista[::2])
print(lista[::-1])
print(lista[:-1])


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)


l1.extend(l2)

print(l1)
print(l2)


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend('a')

print(l1)
print(l2)


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l2.append('b')

print(l1)
print(l2)


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l2.insert(0, 'banana')

print(l1)
print(l2)


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l2.pop()

print(l1)
print(l2)


l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del(l2[3:5])

print(l2)


l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2.insert(0, 'Banana')
print(l2)

del(l2[0])
print(l2)


l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(max(l2))
print(min(l2))


l2 = list(range(0, 100, 8))
print(l2)


l2 = list(range(10))

soma = 0
for valor in l2:
    soma += valor

print(soma)


l2 = ['String', True, 10, -20.5]

for elemento in l2:
    print(f'O tipo de {elemento} e {type(elemento)}')


print('\n\n\n\n')
secreto = 'perfume'
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso n vale.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print('Uma letra ja foi hehe')
    else:
        print('A palavra nao contem essa letra')
        digitadas.pop()

        chances -= 1
        print(f'Chances restantes: {chances}')
        if chances == 0:
            print('Voce perdeu!')
            break

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Voce ganhou! palavra: {secreto_temporario}')
        break
    else:
        print(secreto_temporario)

