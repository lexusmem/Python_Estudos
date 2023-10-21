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
novo_conjunto_2 = {1, 2, 3, 4, 13, 14}
print(type(novo_conjunto))
print(novo_conjunto)
print(type(novo_conjunto_2))
print(novo_conjunto_2)

for i, valor in enumerate(novo_conjunto):
    print(i, valor)

# unir dois conjuntos
# utilizando sinal "|" "ou"
novo_conjunto_uniao = novo_conjunto_2 | novo_conjunto
print(novo_conjunto_uniao)

# verificar dados que constam em ambas as lista:
# Intersecção dos conjuntos:
# Sinal "&"
novo_conjunto_interseccao = novo_conjunto & novo_conjunto_2
print(novo_conjunto_interseccao)

# verificar dados exclusivos em listas:
# Sinal "-"
novo_conjunto_menos = novo_conjunto - novo_conjunto_2
print(novo_conjunto_menos)
# é possível realizar operações de verificação com "in"
print("15 consta no conjunto?", 15 in novo_conjunto_menos)

novo_conjunto_menos_I = novo_conjunto_2 - novo_conjunto
print(novo_conjunto_menos_I)
# é possível realizar operações de verificação com "in"
print("1 consta no conjunto?", 1 in novo_conjunto_menos_I)

# verificar dados ou exclusivos nas listas:
# Que constam exclusivo em cada lista
# Sinal "^"
novo_conjunto_exclusivo = novo_conjunto ^ novo_conjunto_2
print(novo_conjunto_exclusivo)
