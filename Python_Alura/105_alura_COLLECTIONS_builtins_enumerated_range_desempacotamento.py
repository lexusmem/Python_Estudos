idades = [34, 54, 67, 77, 89, 45]

for index, idade in enumerate(idades):  # desempacotador
    print(index, idade)

contador = 0
while contador in range(len(idades)):
    print(contador, idades[contador])
    contador += 1

index_idades_enumerate = list(enumerate(idades))
print(index_idades_enumerate)

index_idades_range = list(range(len(idades)))
print(index_idades_range)

usuarios = [
    ('alex', 39, 1981),
    ('pamela', 24, 1990),
    ('laura', 20, 1995)
]
for index, nome in enumerate(usuarios):
    print(index, nome)

for nome, idade, ano in usuarios:
    print(nome)

for nome, _, _ in usuarios:
    print(nome)
