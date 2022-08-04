from itertools import groupby, tee

alunos = [
    {'nome': 'Paulo', 'nota': 'A'},
    {'nome': 'Henrique', 'nota': 'B'},
    {'nome': 'Joao', 'nota': 'D'},
    {'nome': 'Maria', 'nota': 'A'},
    {'nome': 'Miguel', 'nota': 'B'},
    {'nome': 'Jean', 'nota': 'F'},
    {'nome': 'Saulo', 'nota': 'B'},
    {'nome': 'Jeferson', 'nota': 'A'},
]

orderna = lambda item: item['nota']

alunos.sort(key=orderna)
[print(aluno) for aluno in alunos]

print()
alunos_agrupados = groupby(alunos, orderna)
for agrupamento, valores_agrupados in alunos_agrupados:
    copia, copia2 = tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}')

    quantidade = len(list(copia))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')

    for aluno in copia2:
        print(f'\t {aluno}')
