nome = 'Paulo henrique'
iterador = iter(nome)
gerador = (letra for letra in nome)

print('Gerador: ')
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('O que sobrou do Gerador:')
for item in gerador:
    print(item)

print('O que sobrou depois do for:')
for item in gerador:
    print(item)

print('Iterador: ')
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

print('O que sobrou do Iterador:')
for item in iterador:
    print(item)
