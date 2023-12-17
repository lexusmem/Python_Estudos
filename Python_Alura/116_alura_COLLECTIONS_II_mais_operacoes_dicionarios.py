# Dicionario
# Conjunto de Chave e Valor
# Exemplo: Agenda, Dicionário

telefones = {
    "alex": 12345,
    "testes": 'x23434',
    "rafael": '34566teste'
}

print(telefones)
print(type(telefones))

print('Imprimindo os valores das chaves:')
print(telefones["alex"])
print(telefones["testes"])
print(telefones["rafael"])

# chamando chaves que não constam cadastradas no dicionário.
print(telefones.get('xpto', "Não consta está chave."))

telefones_2 = dict(pamela=43259, laura=98393)
print(telefones_2.keys())

# Incluir elementos no dicionario
telefones['Carlos'] = 134235
print(telefones)

# Alterar valor de alguma chave
telefones['Carlos'] = 12343333
print(telefones)

# Remover uma chave e seu valor
del telefones['testes']
print(telefones)

# verificar se um chave consta no dicionario
print('alex' in telefones)

# como iterar nas chaves dos dicionários:
for chaves in telefones.keys():
    print(chaves)

for chaves in telefones:
    print(chaves)

# como iterar nas valores dos dicionários:
for valores in telefones.values():
    print(valores)

# como iterar nas chaves e valores dos dicionários:
for chaves in telefones.keys():
    valores_chaves = telefones[chaves]
    print(chaves, valores_chaves)

for chave_valor in telefones.items():
    print(chave_valor)

# Desempacotar
for chave, valor in telefones.items():
    print(chave, "=", valor)

# comprehension
print('List Comprehension:')
list_comprehension = ["palavra {}".format(chave) for chave in telefones.keys()]
print(list_comprehension)
