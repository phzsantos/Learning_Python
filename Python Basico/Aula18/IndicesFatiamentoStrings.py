"""
Manipulando strings

* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funcoes built-in len, abs, type, print, etc...

Documentacao:
https://docs.python.org/3/library/functions.html
https://docs.python.org/3/library/stdtypes.html
"""

# positivos
#       [012345678]
texto = 'python s2'
#      -[987654321]
# negativos

url = 'www.google.com.br/'

print(url[:-1])

nova_string = texto[2:6]

print(nova_string)

nova_string = texto[:6]

print(nova_string)

nova_string = texto[7:]

print(nova_string)

nova_string = texto[-1]

print(nova_string)

nova_string = texto[0:6:3]

print(nova_string)

