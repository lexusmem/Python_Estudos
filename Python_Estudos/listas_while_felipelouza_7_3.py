# https://youtu.be/yBeg6s_ybJA

lista1 = [1, 2, 3, 4]
lista2 = ['programação', 'ps', 'py', 'teste']
lista3 = ['oi', 2.0, True, 5, [1, 2]]

# acessar dados ao inverso
print(lista3[-1])
i = -1
print(lista3[i])

# While
i = 0
# acessando os dados da lista com while
while i < len(lista3):
    print(lista3[i])
    i += 1

i = 0
# Alterando dados da lista com while
print(lista2)
while i < len(lista2):
    lista2[i] = 1 + i
    i += 1
print(lista2)
