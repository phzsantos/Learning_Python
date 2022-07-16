def func(arg, arg2):
    return arg * arg2

print(func(3,4))


funcao = lambda x, y: x * y

print(funcao(3,4))


lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

def func(item):
    return item[1]

lista.sort(key=func)

print(lista)


lista.sort(key=lambda item: item[1])

print(lista)


lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista, key=lambda i: i[1]))
print(lista)
