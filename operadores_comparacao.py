# Operador '==' checa a igualdade
print(2 == 2)

# Operador '>' maior do que
print(2 > 2)

# Operador '<' menor do que
print(2 < 2)

# Operador '<=' menor ou igual do que
print(2 <= 2)

# Operador '>=' maior ou igual do que
print(2 >= 2)

# Operador '!=' diferente
print(2 != 2)

nome = input('Qual o seu nome: ')
idade = int(input('Qual a sua idade: '))

# Idade limite para pegar empréstimo
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome.capitalize()} pode pegar empréstimo.')
else:
    print(f'{nome.capitalize()} NÃO PODE PEGAR EMPRÉSTIMO.')
