idades = [34, 54, 67, 77, 89, 45]
# Ordenar os números
print(idades)
print(list(reversed(idades)))
print(sorted(idades))
print(sorted(idades, reverse=True))
print(list(reversed(sorted(idades))))

# lista é mutável .sort() or .reverse() altera
# as ordens dos atributos dentro da variável
print(idades)
idades.sort(reverse=True)
# alterar a ordem
# idades.reverse()
print(idades)
