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
