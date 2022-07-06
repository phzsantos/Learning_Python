logged_user = False

if logged_user:
    mensagem = 'Usuario logado'
else:
    mensagem = 'Usuario precisa logar'

print(mensagem)


mensagem = 'Usuario logado' if logged_user else 'Usuario precisa logar'

print(mensagem)


idade = 17

print('Pode acessar') if idade >= 18 else print('Nao pode acessar')


idade = int(input('Qual sua idade: '))

print('Pode acessar') if idade >= 18 else print('Nao pode acessar')
