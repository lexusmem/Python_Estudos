import requests
from alura_cep import BuscaEndereco

# Instanciando o atributo CEP e validando com classe
cep = "04177250"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

dados_cep = objeto_cep.acessa_via_cep()
print(dados_cep)

#  TESTES REALIZADOS ABAIXO:
# print(a.text)
# print(a.json())
# print(a.json()['cep'])
# r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
# print(r)
# print(r.status_code)  # Retorna o código da requisição http
# print(type(r))
# # print(dir(r))
# print(r.text)

# # Transformando o retorno do request em um dict
# json = r.json()
# print(json)
# print(type(json))
# for chave in json.keys():
#     print(chave)
# for valor in json.values():
#     print(valor)
# for chave, valor in json.items():
#     print(chave, valor)
