from alura_MetodosSTRINGS_extratorArgumentosURL import ExtratorArgumentosURL

url = 'https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor'\
      '=1500'

argumentoUrl = ExtratorArgumentosURL(url)
print(argumentoUrl.url)

moedaOrigem, moedaDestino = argumentoUrl.extraiArgumentos()
print(f'A moeda de origem é o {moedaOrigem}.')
print(f'A moeda de destino é o {moedaDestino}.')
