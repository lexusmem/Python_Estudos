# Alterando conjuntos são mutáveis
usuarios = {1, 5, 76, 54, 34, 52, 22, 17}

print(usuarios)
print(len(usuarios))

# Adicionar elementos na lista
usuarios.add(18)

print(usuarios)
print(len(usuarios))

# para congelar a lista para não incluir mais dados:
# usuarios = frozenset()
# usuarios.add(345)
# print(usuarios)

meu_texto = 'Bem vindo meu nome é Alex gosto muito de nome e tenho '\
            'muito cachorro Alex.'
print(meu_texto)

conjunto_meu_texto = set(meu_texto.split())
print(conjunto_meu_texto)
