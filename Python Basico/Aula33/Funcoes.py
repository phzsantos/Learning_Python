def funcao():
    print('Ola mundo!')

funcao()
funcao()
funcao()
funcao()

print('Hello world')
print('Hello world')
print('Hello world')
print('Hello world')


def funcao(msg):
    print(msg)

funcao('Mensagem')


def saudacao(msg='Olá', nome='usuario'):
    nome = nome.replace('a', '4')
    print(msg, nome)

saudacao('Olá', 'Paulo')
saudacao()
saudacao(nome='Paulo', msg='Hi')


def saudacao(msg='Olá', nome='usuario'):
    nome = nome.replace('a', '4')
    return f'{msg} {nome}'

variavel = saudacao()
print(variavel)