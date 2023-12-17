idade1 = 39
idade2 = 39
idade3 = 39
# coleções - diversos valores  - list
idades = [12, 40, 34, 36, idade1, idade2]

print(idades)
# tipo da variável lista
print(type(idades))
# Tamanho das listas Len()
print(f'Tamanho da lista - {len(idades)}')
# Acessando os elementos
print(idades[0])
print(idades[5])
# Lista pode alterar e adicionar elemetos
# append() adicionar elemento ao final da lista
idades.append(idade3)
print(idades)
# remove() remover elemento da lista
# remove o primeiro elemento duplicado
idades.remove(idade3)
print(idades)
# remover todos os elementos
idades.clear()
print(idades)
