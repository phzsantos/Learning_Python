"""
str = Strings                - "Isso" 'Isso!'
int = Inteiros               - 10 20 30 -1
float = real/ponto flutuante - 1.5 2.7 -1.4
bool = booleano/logico       - True/False
"""

print(type('Paulo'))
print(type(1))
print(type(1.1))
print(type(False))

print('10', type('10'), int('10'), type(int('10')))
print(bool(0))
print(bool(1))
print(float('10.5'))
print(int(10.5))
print(float('10'))  # pode converter inteiro em string para float
#print(int('10.5'))  # nao pode converter ponto flutuante em string para inteiro direto

print('Paulo', type('Paulo'))
print(20, type(20))
print(1.75, type(1.75))
print(20 > 18, type(20 > 18))
