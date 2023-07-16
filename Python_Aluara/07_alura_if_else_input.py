print('==================================')
print('Bem vindo ao jogo de adivinhação!')
print('==================================')

numero_secreto = 33

while True:
    numero_usuario = input('Digite o número secreto: ')
    if numero_usuario.capitalize() == 'S':
        print('Sair.')
        break
    elif int(numero_usuario) == numero_secreto:
        print('Você acertou!')
        break
    else:
        print('Errou! Tente novamente.')
        print('Para sair digite "S".')
