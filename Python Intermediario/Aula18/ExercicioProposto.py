carrinho = []
carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 2', 50))

preco_total = sum([item[1] for item in carrinho])
print(preco_total)


total = sum([float(y) for x, y in carrinho])
print(total)