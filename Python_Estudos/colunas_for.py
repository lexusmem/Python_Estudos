matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

linhas_matriz = range(len(matriz))

for i in range(len(matriz)):
    column_size = range(len(matriz[i]))
    for column in column_size:
        print(f'==========column {column}================')
        for linha in linhas_matriz:
            print(matriz[linha][column])
    break

for lin in linhas_matriz:
    columns = range(len(matriz[lin]))
    print(f'=====linha {lin}========')
    for col in columns:
        print(matriz[lin][col])
