from collections import defaultdict
# Dicionario
# Conjunto de Chave e Valor
# Exemplo: Agenda, Dicionário

meu_texto = 'Bem vindo alex meu nome é Alex gosto muito de nome e tenho '\
            'muito cachorro Alex'
#  minuscula
meu_texto = meu_texto.lower()

# separar por palavras meu texto usa o split
aparicoes_1 = {}

# Realizar contagem de um texto
# utilizando dicionarios

# SEM a função defaultdict
for palavra in meu_texto.split():
    ate_agora = aparicoes_1.get(palavra, 0)
    aparicoes_1[palavra] = ate_agora + 1

print(aparicoes_1)

# COM a função defaultdict
aparicoes_2 = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparicoes_2[palavra]
    aparicoes_2[palavra] = ate_agora + 1

print(aparicoes_2)
