import sys
import time

lista = [0,1,2,3,4,5,6]

print(hasattr(lista, '__iter__'))
print(hasattr(lista, '__next__'))


lista = list(range(10))

print(sys.getsizeof(lista))


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()

print(g)

print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))

print(next(g))
print(next(g))
print(next(g))


def gera():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel


g = gera()

print(next(g))
print(next(g))
print(next(g))


lista = [x for x in range(1000)]
print(type(lista))
lista = (x for x in range(1000))
print(type(lista))


l1 = [x for x in range(10000)]
l2 = (x for x in range(10000))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

