def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6

var = func(1,2,3,4,5, nome='Luiz', a6='5')

print(var)
print(var[0], var[1])


def func_args(*args):
    print(args)
    print(args[0])
    print(args[-1])
    args = list(args)
    args[0] = 20
    print(args)

lista = [1, 2, 3, 4, 5]

print(*lista)
print(*lista, sep='-')

func_args(1, 2, 3, 4, 5)


def func_args_2(*args):
    print(args)

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

func_args_2(lista)
func_args_2(*lista, *lista2)


def func_args_kwargs(*args, **kwargs):
    print(args)

    idade = kwargs['idade']  # se nao existir esse campo, da erro
    idade = kwargs.get('idade')  # nao da erro se nao existir

    if idade:
        print(idade)

func_args_kwargs(*lista, *lista2, idade=30)
