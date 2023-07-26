# https://youtu.be/HVd46cZbmgM

lista = ['a', ['b', ['c', 'cc'], 'bb'], 'd', ['e', 'f'], 'g']
print(lista[0])  # a
print(lista[1])  # ['b', ['c', 'cc'], 'bb']
print(lista[1][0])  # b
print(lista[1][1])  # ['c', 'cc']
print(lista[1][1][0])  # c
print(lista[3])  # ['e', 'f']
print(lista[3][0])  # e
print(lista[3][1])  # f
print(lista[1][1][0])  # c

# Matriz 2d
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(type(m))  # <class 'list'>
print(type(m[0]))  # <class 'list'>
print(type(m[0][0]))  # <class 'int'>
