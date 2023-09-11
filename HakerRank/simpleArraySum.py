def somar(lista):
    soma = 0
    for valor in lista:
        soma = soma + valor
    return soma


lista = [1, 2, 10]

print(somar(lista))
