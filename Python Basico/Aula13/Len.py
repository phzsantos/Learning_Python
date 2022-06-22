usuario = input('Digite seu usuario: ')

qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Quantidade de caracteres invalida.')
else:
    print('Cadastrado no sistema.')

string1 = input('String1: ')
string2 = input('String2: ')

print(f'A quantidade total de caracteres digitados foi: {len(string1)+len(string2)}')
