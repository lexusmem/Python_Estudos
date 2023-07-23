"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # Função str
* Join - Unir lista # Função str
* Enumerate - Enumerar elementos de uma lista # list/Objetos Iteráveis
"""
string = 'O Brasil é o pais do futebol, o Brasil é Penta!'

# A função split cria uma lista com elementos de uma string.
lista1 = string.lower().split(' ')
lista2 = string.lower().split(',')

print(f'Lista 1 -> {lista1}')
print(f'Lista 2 -> {lista2}')

# A função join une os elementos de uma lista em uma string
string1 = ' '.join(lista1)
print(f'Nova string criada a partir da lista 1 -> "{string1.capitalize()}"')

# A função Enumerate lista o índice da lista.
for indice, numero in enumerate(lista1):
    print(indice, numero)

# o método count verifica dentro de cada índice
# da lista se consta a busca desejada
print(lista1.count('futebol,'))
print(lista2.count('brasil'))


for valor in lista1:
    print(f'A palavra "{valor.upper()}" aparece {lista1.count(valor.lower())}'
          'x na frase.')

palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor.lower())

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra "{palavra.upper()}" repetiu mais vezes {contagem}x.')
