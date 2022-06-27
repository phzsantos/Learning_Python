frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0

while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1

contador = 0
nova_string = ''

while contador < tamanho_frase:
    nova_string += frase[contador]
    print(nova_string)
    contador += 1

contador = 0
nova_string = ''
letra = input('Letra a capitular: ')

while contador < tamanho_frase:
    if letra == frase[contador]:
        nova_string += letra.upper()
    else:
        nova_string += frase[contador]

    contador += 1

print(nova_string)
