"""
For / Else
"""

variavel = ['Alex Sousa', 'Pamela Rodrigues',
            'Gabriel Sousa', 'Bryan Sousa', 'Laura Sousa']

for nome in variavel:
    print(nome)
    for letra in nome:
        print(letra)

for nome in variavel:
    if nome.startswith('A'):
        print(nome, '- Começa com a letra "A".')
    else:
        print(nome, '- Não começa com a letra "A".')

primeira_leta_B = False
for nome in variavel:
    if nome.lower().startswith('b'):
        primeira_leta_B = True

if primeira_leta_B:
    print('Existe uma palavra que começa com J')
else:
    print('Não existe uma palavra que começa com J')

palavra = 'x'
for nome in variavel:
    if nome.lower().startswith(palavra):
        print(f'Existe palavra que começa com "{palavra.upper()}" - ', nome)
        break
else:
    print(f'Não existe palavra que começa com "{palavra.upper()}".')
