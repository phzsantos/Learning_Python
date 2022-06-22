"""
Documentacao: https://docs.python.org/3/library/stdtypes.html
Funcoes Luiz: https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py
"""
import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


num1 = input('Primeiro: ')
num2 = input('Segundo: ')

# isnumeric isdigit isdecimal
# numeros inteiros apenas e positivos
print(num1.isnumeric())
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Nao deu pra somar :(')

try:
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
except:
    print('Erro :(')
