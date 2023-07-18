dias = int(input('Informe o numero de dias trabalhados: '))

soma = 0
x = 1
soma_notas = 0.00

while x <= dias:
    notas = float(input(f'Informe o valor do dia n° {x}: '))
    soma_notas += notas
    x += 1

print(f'Valor total a ser pago é de {soma_notas}')
