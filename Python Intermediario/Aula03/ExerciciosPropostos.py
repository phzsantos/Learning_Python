"""
1 - Crie uma funcao que exibe uma saudacao com os parametros saudacao e nome.
"""

def saudacao(msg='Ola', nome='Desconhecido'):
    print(msg, nome)

saudacao('Oi', 'Paulo')


"""
2 - Crie uma funcao que recebe 3 numeros como parametros e exiba a soma entre eles.
"""

def soma_trio(numero1, numero2, numero3):
    print(numero1 + numero2 + numero3)

soma_trio(1, 3, 5)


"""
3 - Crie uma funcao que receba 2 numeros. O primeiro é um valor e o segundo um percentual (ex. 10%). retorne (return) o valor do primeiro numero somado do aumento do percentual do mesmo. 
"""

def aumento(valor_bruto, percentual):
    return valor_bruto + valor_bruto * percentual / 100

aumento = aumento(1200, 50)

print(aumento)


"""
4 - Fizz buzz - se o parametro da funcao for divisel por 3, retorne fizz. Se o parametro da funcao for divisivel por 5, retorne Buzz. Se o parametro da funcao for divisivel por 5 e por 3, retorne FizzBuzz, caso contrario, retorne o numero enviado.
"""

def FizzBuzz(valor):
    if not valor % 3 and not valor % 5:
        return 'FizzBuzz'
    
    if not valor % 3:
        return 'Fizz'
    
    if not valor % 5:
        return 'Buzz'

    return valor

fizz_buzz = FizzBuzz(15)

print(fizz_buzz)
