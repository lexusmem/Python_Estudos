def miniMaxSum(arr):

    soma = 0
    lista_nova = []

    for i, qtd in enumerate(arr):
        for valor in arr:
            soma += valor

        lista_nova.append(soma-arr[i])
        soma = 0
    return print(min(lista_nova), max(lista_nova))


miniMaxSum([1, 3, 5, 7, 9])
