d1 = {'chave1':'valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'

print(d1['chave1'])


d1 = dict(chave1='valor da chave', chave2='valor da outra chave')
d1['nova_chave'] = 'Valor da nova chave'

print(d1)


d1 = {'chave1': 'valor da chave', 'chave1': 'valor da chave', 'chave1': 'valor real da chave'}

print(d1)


d1 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla',
}

print(d1[(1,2,3,4)])

# print(d1['Nao existe'])  # retorna erro e para o codigo se a chave n existir

print(d1.get('nomedachave'))  # retorna none e o codigo continua

d1[(1,2,3,4)] = 'tupla'

print(d1[(1,2,3,4)])

print(d1)

del d1[(1,2,3,4)]

print(d1)

print('str' in d1)
print('str' in d1.keys())  # mesma coisa do de cima
print('valor' in d1.values())

print(len(d1))

d1 = {
    'Chave1' : 'valor',
    'Chave2' : 'Outro valor',
    'chave3' : 'Tupla',
}

for k, v in d1.items():
    # print(k[0], k[1]) pode ser assim
    print(k, v)


clientes = {
    'cliente1' : {
        'nome' : 'Paulo',
        'Sobrenome' : 'Henrique',
    },
    'Cliente2' : {
        'nome': 'Luiz',
        'Sobrenome': 'Otavio',
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')


d1 = {1 : 'a', 2 : 'b', 3: 'c'}
v = d1

v[1] = 'Paulo'

print(d1)
print(v)

d1 = {1 : 'a', 2 : 'b', 3: 'c'}
v = d1.copy()  # para fazer uma copia que n altera os valores, a nao ser que sejam listas

v[1] = 'Paulo'

print(d1)
print(v)

d1 = {1 : 'a', 2 : 'b', 3: 'c', 'd' : ['Luiz', 'Henrique']}
v = d1.copy()

v['d'][0] = 'Paulo'

print(d1)
print(v)

import copy

d1 = {1 : 'a', 2 : 'b', 3: 'c', 'd' : ['Luiz', 'Henrique']}
v = copy.deepcopy(d1)

v['d'][0] = 'Paulo'

print(d1)
print(v)


lista = [  # tbm funciona se for tupla
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)

print(d1)


d1 = {
    1: 2,
    2: 3,
    4: 5,
}

d1.pop(4)
d1.popitem()
print(d1)


d1 = {
    1: 2,
    2: 3,
    4: 5,
}

d2 = {
    'a': 'b',
    'c': 'd',
}

print(d1)
print(d2)
d1.update(d2)
print(d1)
