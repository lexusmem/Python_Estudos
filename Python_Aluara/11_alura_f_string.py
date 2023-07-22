print('==================================')
print('Bem vindo ao jogo de adivinhação!')
print('==================================')

numero_secreto = 33
tentativas = 3

while True:

    numero_usuario = input('Digite o número secreto: ')

    sair = numero_usuario.capitalize() == 'S'

    if sair:
        print('Sair.')
        break

    if not numero_usuario.isnumeric():
        print('Valor Inválido. Digite um número.')
        continue

    acertou = int(numero_usuario) == numero_secreto
    numero_maior = int(numero_usuario) > numero_secreto
    numero_menor = int(numero_usuario) < numero_secreto

    if acertou:
        print('Você acertou!\n'
              '====Fim de Jogo====')
        break
    else:
        tentativas -= 1
        if tentativas <= 0:
            print('Você perdeu!')
            break

        if numero_maior:
            print('Errou! O número digitado é maior que o número secreto.'
                  ' Tente novamente.')
            print('Para sair digite "S".')
        elif numero_menor:
            print('Errou! O número digitado é menor que o número secreto.'
                  ' Tente novamente.')
            print('Para sair digite "S".')

        if tentativas == 1:
            print('Última tentativas!')
        else:
            print(f'Você possuí {tentativas} tentativas.')
