matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12, 11],
]

column_size = range(len(matriz[0]))
linhas_matriz = range(len(matriz))

for column in column_size:
    print(f'==========column {column}================')
    for linha in linhas_matriz:
        print(matriz[linha][column])

for lin in linhas_matriz:
    columns = range(len(matriz[lin]))
    print(f'=====linha {lin}========')
    for col in columns:
        print(matriz[lin][col])

print('==========WHILE============')

linha = 0
qtd_linha = len(matriz)

while linha < qtd_linha:
    # print(matriz[linha])
    colunas = 0
    qtd_colunas = len(matriz[linha])
    print(f'==========Linha {linha}============')
    while colunas < qtd_colunas:
        print(matriz[linha][colunas])
        colunas += 1
    linha += 1
