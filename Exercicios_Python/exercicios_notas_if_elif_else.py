# aprovado - >= 7
# reprovado - < 7
# Aprovado com distinção - média = a 10

provas = int(input('Quantas provas existem? '))

x = 1
notas = 0.0
soma_notas = 0.0

while x <= provas:
    notas = float(input(f'Informe a nota n° {x}: '))
    x += 1
    soma_notas += notas

media = soma_notas / provas

if media >= 7 and media < 10:
    print(f'Aprovado, sua média foi {media: .2f}.')
elif media < 7:
    print(f'Reprovado, sua média foi {media: .2f}.')
elif media == 10:
    print(f'Aprovado - PARABÉNS, sua média foi {media: .2f}.')
