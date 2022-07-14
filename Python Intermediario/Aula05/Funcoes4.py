"""
Nao pode acessar uma variavel de uma funcao diretamente na outra
Nao pode trocar o valor de uma variavel global localmente depois de ter usado ela anteriormente
Pode acessar todas as variaveis globais, mas quando for trocar de valor ele vai criar uma local
Pode mexer com as variaveis globais de dentro de funcoes, mas nao e boa pratica.
"""

variavel = 'valor'

def func():
    print(variavel)


def func2():
    # global variavel nao e uma boa pratica
    variavel = 'Outro valor'
    print(variavel)


def func3(arg=None):
    arg = arg.replace('v', 'c')
    return arg


func()
func2()
outra_variavel = func3(variavel)

print(variavel)
print(outra_variavel)


def func4():
    outra_variavel = 'Paulo Henrique'
    return outra_variavel


def func5(arg):
    print(arg)


var = func4()
func5(var)
