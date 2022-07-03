variavel = ['Luiz Otavio', 'Joaozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):
        print(f'{valor} Comeca com j')
    else:
        print(f'{valor} Nao comeca com j')


comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe palavra que comeca com j')
else:
    print('Nao existe palavra que comeca com j')


for valor in variavel:
    if valor.lower().startswith('j'):
        print('Existe palavra que comeca com j')
        break
else:
    print('Nao existe palavra que comeca com j')

