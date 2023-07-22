"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # Função str
* Join - Unir lista # Função str
* Enumerate - Enumerar elementos de uma lista # list/Objetos Iteráveis
"""
string = 'O Brasil é o pais do futebol, o Brasil é Penta!'

lista1 = string.lower().split(' ')
lista2 = string.lower().split(',')

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

# A função join une os elementos de uma lista
print(lista1)
string1 = ' '.join(lista1)
print(string1.capitalize())

# A função enumerate mostra o numero do índice.
for indice, valor in enumerate(lista1):
    print(indice, valor)

lista3 = [
    [1, 2],
    [3, 4],
    [5, 6]
]
for indice, x in enumerate(lista3):
    print(indice, x)

for x in lista3:
    print(x[0])
