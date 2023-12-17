from collections import defaultdict, Counter
# Dicionario
# Conjunto de Chave e Valor
# Exemplo: Agenda, Dicionário

meu_texto = 'Bem vindo alex meu nome é Alex gosto muito de nome e tenho '\
            'muito de cachorro de Alex'
#  minuscula
meu_texto = meu_texto.lower()

# Realizar contagem de um texto
# utilizando dicionários

# COM a função defaultdict
aparicoes_2 = defaultdict(int)
for palavra in meu_texto.split():
    aparicoes_2[palavra] = aparicoes_2[palavra] + 1
print(aparicoes_2)

#  Ou

aparicoes = Counter(meu_texto.split())
print(aparicoes)


dicionario = {"alex": 1}
print(dicionario)
print(dicionario['alex'])
teste = dicionario['alex']
dicionario['alex'] = dicionario['alex'] + 1
dicionario['alex'] += 1
print(dicionario['alex'])
print(teste)
dicionario['alex_2'] = 0
print(dicionario)
