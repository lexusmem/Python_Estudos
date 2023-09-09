'''
Desempacotamento
'''
lista_1 = [1, 2, 3]
x1, x2, x3 = lista_1
print(x1, x2, x3)

lista = ['luiz', 'alex', 'renata', 'camila', 1, 2, 3, 4, 5, 6]
n1, n2, *outra_lista, ultimo_da_lista = lista
print(n2)
print(outra_lista)
print(ultimo_da_lista)

*outra_lista, penultimo_da_lista, ultimo_da_lista = lista
print(penultimo_da_lista)
