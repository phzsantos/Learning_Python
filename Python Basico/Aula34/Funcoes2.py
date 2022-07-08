def funcao(var):
    print(var)

funcao('Valor que eu quero')


variavel = funcao('teste')

print(type(funcao('teste')))

if variavel:
    print(variavel)
else:
    print('Nenhum valor')


def funcao(var):
    return var
    print('Isso nao sera executado')

variavel = funcao('Teste com return')

print(type(funcao('teste')))

if variavel:
    print(variavel)
else:
    print('Nenhum valor')


def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8, 2)

if divide:
    print(divide)
else:
    print('Conta invalida.')


def dumb():
    return 1

print(dumb(), type(dumb()))


def f(var):
    print(var)

def dumb():
    return f

variavel = dumb()('Sim, está executando')

variavel = dumb()
print(type(variavel), id(f), id(variavel))
variavel('Ola!')


def dumb():
    return 'Paulo', 'Henrique'

var = dumb()

print(var[0], var, type(var))
