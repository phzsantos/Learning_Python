contador2 = 10
for contador1 in range(9):
    print(contador1, contador2)
    contador2 -= 1


print()
for progressivo, regressivo in enumerate(range(10, 1, -1)):
    print(progressivo, regressivo)
