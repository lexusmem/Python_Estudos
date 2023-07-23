#  Assert é uma estrutura do python
# verifica que uma condição está sendo satisfeita
# para garantir a continuação código
# Usado na construção, no desenvolvimento do código
import requests
print('Início')
# Assert inserido em uma parte do código para
# verificar se uma condição esta sendo aplicada
assert 1 < 2
print('Final')

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
requisicao_dic = requisicao.json()

cotacao = requisicao_dic['USDBRL']['bid']
cotacao = float(cotacao)
print('Cotação do Dolar x Real =', cotacao)

preco_produto = 100

assert type(cotacao) == float
assert cotacao > 0
faturamento = preco_produto * cotacao
print(faturamento)
