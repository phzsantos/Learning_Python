"""
+  - Adicao
-  - Subtracao
*  - Multiplicacao
/  - Divisao
// - Divisao inteira
** - Exponenciacao
%  - Resto/modulo
() - Parenteses

Precedencia: 1 (),
             2 **,
             3 *, /, //, %
             4 + -

Operadores de mesma precedencia sao lidos da esquerda para direita.
"""

print(20 * 'A')
print('10' + '10')

print('Paulo ' + 'Tem ' + str(20) + ' Anos')

print('Adicao +', 10 + 10)
print('Subtracao -', 10 - 5)
print('Multiplicao *', 10 * 10)
print('Divisao /', 10 / 2)
print('Divisao inteira //', 10 // 3)
print('Exponenciacao **', 2 ** 10)
print('Modulo %', 10 % 2)

print(5+2*10)
print((5+2)*10)
