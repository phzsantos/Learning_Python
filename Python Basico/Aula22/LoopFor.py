"""
Usado para situacoes envolvendo coisas finitas
for range(start=0, stop, step=1)
"""

texto = 'Python'

for letra in texto:
    print(letra)

for numero in range(10):
    print(numero)

for numero in range(20, 10, -1):
    print(numero)

for numero in range(0, 100, 8):
    print(numero)

nova_string = ''

for letra in texto:
    if letra == 't' or letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
