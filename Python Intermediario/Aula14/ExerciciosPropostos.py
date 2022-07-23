string = '012345678901234567890123456789012345678901234567890123456789'

lista = [string[index:index+10] for index, numero in enumerate(string) if numero == '0']
print(lista)
final = [print(f'{item}.', end='') if index != len(lista)-1 else print(f'{item}') for index, item in enumerate(lista)]


n = 10
comp = [string[i:i+n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(comp)
print(retorno)
