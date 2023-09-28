from alura_MetodosSTRINGS_extratorArgumentosURL import ExtratorArgumentosURL

argumento = 'bytebank.com/cambio?moedaorigem=real'
# Método find() localiza um carácter
# em um conjunto de string
# e retorno o seu índice
index = argumento.find("=")
substring = argumento[index + 1:]
print(substring)

# Método split() cria vetores
# separando as strings
# através de um argumento
listaargumentos = argumento.split("=")
print(listaargumentos[1])

# None - não possuí valor
string = None
if string:
    print('Tem algo aqui.')
else:
    print('Não tem nada aqui.')

string = ""
if string:
    print('Tem algo aqui.')
else:
    print('Não tem nada aqui.')

string = "None"
if string:
    print('Tem algo aqui.')
else:
    print('Não tem nada aqui.')

url = 'https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor'\
      '=1500'
print(ExtratorArgumentosURL.urlEhvalida(url))
