"""
Listas em python
https://youtu.be/CSTb7pLsLZE
Fatiamento
append, insert, pop, del, clear,
extend, + , min, max
range
"""

# para criação de lista utiliza colchetes [].
# na lista pode conter qualquer tipo de dados.
exemplo = [1, 2, 3, 4, 'Alex Sousa', True, False]

# para acessar os dados de uma lista deve-se pelo índice.
#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E']
#         -5  -4   -3   -2   -1

# imprimir uma lista
print(lista)

# acessar um dado da lista
print(lista[4])

# tamanho da lista
print(len(lista))

# Alterar uma dado do índice através do índice.
lista[4] = 'Qualquer coisa'
print(lista)

# Fatiamento
print(lista[0:3])
print(lista[:3])
print(lista[2:])
# Último item da lista
print(lista[-1])
# Primeiro item da lista
print(lista[0])
# Passos para impressão
print(lista[::2])
# Inverte lista
print(lista[::-1])

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l3 = l1 + l2

l1.extend(l2)
l1.extend('a')  # type: ignore

# Append insere um novo valor no final da lista
l2.append('b')  # type: ignore

# Insert função para inserir um novo valor um índice determinado
l2.insert(0, 'banana')  # type: ignore

print(l1)
print(l2)
print(l3)

# Pop função remove último elemento da lista
l2.pop()
print(l2)

l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l4)

# Del função remove trecho da lista
del (l4[3:5])
print(l4)
del (l4[-1])
print(l4)

# Funções para verificar valor mínimo e máximo
print(max(l4))
print(min(l4))

# Utilizando a função range para gerar dados em uma lista
l5 = list(range(0, 100, 8))
print(l5)

# É possível iterar sobre a lista
for valor in l5:
    print(valor)

soma = 0
for valor in l5:
    soma = soma + valor
print(soma)

l6 = ['String', True, 10, -20.10]

for elem in l6:
    print(f'O tipo do índice {l6.index(elem)} é {type(elem)} '
          f'e seu valor é {elem}.')

# Index função para retornar o índice de um valor
print(l6.index(10))


print('======Jogo Forca=====')

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você Perdeu!')
        break

    letra = input('Digite uma palavra: ')

    if len(letra) > 1:
        print('Digite apenas uma palavra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" digitada existe na palavra secreta.')
    else:
        print(f'A letra "{letra}" digitada NÃO existe na palavra secreta.')
        digitadas.pop()
        chances -= 1

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Você acertou a palavra secreta! "{secreto.upper()}"')
        break

    print(f'A palavra secreta está assim: {secreto_temporario}.')
    print(f'Você possuí {chances} chances.')
