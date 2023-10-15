usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 53, 56, 42]

assistiram = []

# criado nova variável para unir as
# duas listas acima
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(type(assistiram))
print(assistiram)
print(id(usuarios_data_science))
print(id(assistiram))

# para descartar os valores duplicados da nova lista
# transformar em conjunto "Set"
assistiram_set = set(assistiram)
print(assistiram_set)
print(type(assistiram_set))
print(id(assistiram_set))

# outra forma de criar um conjunto:
# não guarda ordem nos elementos
# não existe posição em um conjunto(set)
novo_conjunto = set([10, 12, 13, 14, 14])
novo_conjunto_2 = {1, 2, 3, 4}
print(type(novo_conjunto))
print(novo_conjunto)
print(type(novo_conjunto_2))
print(novo_conjunto_2)

for i, valor in enumerate(novo_conjunto):
    print(i, valor)

# unir dois conjuntos
# utilizando "ou"
novo_conjunto_ou = novo_conjunto_2 | novo_conjunto
print(novo_conjunto_ou)
