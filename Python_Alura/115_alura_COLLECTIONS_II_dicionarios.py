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
