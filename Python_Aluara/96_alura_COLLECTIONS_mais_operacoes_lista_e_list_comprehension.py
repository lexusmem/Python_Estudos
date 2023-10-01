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
# Lista pode alterar e adicionar elementos
# append() adicionar elemento ao final da lista
idades.append(idade3)
print(idades)
# remove() remover elemento da lista
# remove o primeiro elemento duplicado
idades.remove(idade3)
print(idades)
# remover todos os elementos
# idades.clear()
print(idades)
# In para verificar se um elemento faz parte da lista
print(28 in idades)
# If para verificar se elemento consta antes de remover
if 15 in idades:
    idades.remove(15)
print(idades)
# Inserir elemento no local desejado
idades.insert(0, 19)
print(idades)
# Adicionar mais de um elemento
idades.extend([15, 87, 55])
print(idades)
# Acessar elementos de uma lista com for
for elementos in idades:
    print('Recebi o elemento', elementos)
# Iteração para criar nova lista e somar 1
print(idades)
idades_novo_ano = []
for idade in idades:
    idades_novo_ano.append(idade + 1)
print(idades_novo_ano)
# nova forma para iterar e somar valores
# LIST COMPREHENSION
idades_novo_ano_2 = [(idade+1) for idade in idades_novo_ano]
print(idades_novo_ano_2)
maior_idade = [(idade) for idade in idades_novo_ano_2 if idade >= 18]
print(maior_idade)
