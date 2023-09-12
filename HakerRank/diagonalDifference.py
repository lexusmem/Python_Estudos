def diagonalDifference(arr):
    lin = 0
    num_linhas = len(arr)

    col = 0
    nun_colunas = len(arr[0])

    soma_principal = 0
    soma_secundaria = 0

    while lin < num_linhas:
        soma_principal += arr[lin][lin]
        col = 0
        while col < nun_colunas:
            if col + lin == nun_colunas - 1:
                soma_secundaria += arr[lin][col]
            col += 1
        lin += 1
    return abs(soma_principal - soma_secundaria)


x = [[11, 2, 4],
     [4, 5, 6],
     [10, 8, -12]]

print(diagonalDifference(x))
