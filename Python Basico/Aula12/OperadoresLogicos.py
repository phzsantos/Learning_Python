"""
and, or, not, in, not in
"""

a = 2
b = 2
c = 3

expressao = a == b and b < c

print(expressao)

primeiro = 0
segundo = 3

if not primeiro:
    print('preencha')
else:
    print('roda')

nome = 'Paulo'

if 'asdf' in nome:
    print('ta no nome')
else:
    print('nao ta')

texto = '2 palito'

if 'asdf' not in nome:
    print('executa')
else:
    print('passa')

usuario = input('Usuario: ')
senha = input('Senha: ')

usuario_db = 'admin'
senha_db = '123456'

if usuario_db == usuario and senha_db == senha:
    print('Acesso permitido.')
else:
    print('Acesso negado.')
