"""
1 - Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada
"""

def func(arg):
    return arg()

def func2():
    return 'Bom dia'

print(func(func2))

"""
2 - Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada. Faca a funcao1 executar duas funcoes que recebam um numero diferente de argumentos 
"""

def func(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def func2(nome):
    return f'Oi {nome}'

def func3(nome, mensagem):
    return f'{mensagem} {nome}'

print(func(func2, 'Paulo'))
print(func(func3, 'Paulo', mensagem='Bom dia'))
