# Supondo que matriz é uma lista de listas representando a matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

num_columns = len(matriz[0])

for col in range(num_columns):
    print(f'Coluna {col}.')
    for row in matriz:
        print(row[col])
    print()
