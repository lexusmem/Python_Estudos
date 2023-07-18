# Estrutura básica do loop While
x = 0  # contador
while x < 5:  # condição para executar while
    print(x)
    x += 1  # soma contador
print('Fim do primeiro While\n')

# Estrutura loop While com acumulador
contador = 1  # contador
acumulador = 1
while contador <= 5:  # condição para executar while
    print(contador, acumulador)
    acumulador = acumulador + contador  # soma acumulador
    contador += 1  # soma contador
print('Fim do While com acumulador\n')

# While com else
contador = 0

while contador < 10:
    contador += 1
    print(f'Valor do contador é {contador}')
else:
    print(f'Fim do while com else. O valor do contador é {contador}.\n')

# While com continue
x = 0  # contador
while x < 5:  # condição para executar while
    if x == 3:  # estrutura para excluir um dos itens para do loop
        x += 1
        continue  # estrutura para excluir um dos itens para do loop
    print(x)
    x += 1  # soma contador
print('Fim do While com continue.\n')

# While com break
x = 0  # contador
while x < 5:  # condição para executar while
    if x == 3:  # estrutura para parar o loop em um determinado parâmetro
        x += 1
        break  # estrutura para parar o loop em um determinado parâmetro
    print(x)
    x += 1  # soma contador
print('Fim do While com Break.\n')

# While com While
c = 0  # valor da coluna
while c < 5:  # condição para executar o primeiro while
    lin = 0  # valor de linha
    while lin < 5:  # condição para executar o segundo while
        print(f'({c},{lin})')
        lin += 1
    c += 1
print('Fim do While com While.\n')

# While com continue e break
x = 0
while x < 10:
    if x == 3:
        x += 1
        continue  # Pula a iteração quando x = 3
    if x == 6:
        break  # Interrompe o loop quando x = 6
    print(x)
    x += 1

# While com loop Infinito
# Criação Calculadora
while True:

    num_1 = input('Informe o primeiro número: ')
    num_2 = input('Informe o segundo número: ')
    operador = input('Informe tipo da operação matemática: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Erro - Informe números para cálculo.')
        continue

    num1 = int(num_1)
    num2 = int(num_2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    else:
        print('Erro - Operador Inválido!')

    print('Para interromper o program digite "Crtl + C".')
