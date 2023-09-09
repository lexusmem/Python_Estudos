print('==================================')
print('Bem vindo ao jogo de adivinhação!')
print('==================================')

numero_secreto = 33
tentativas = 3

for n in range(1, tentativas + 1):

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
        if n == 3:
            print('Você perdeu!')
            break

        if numero_maior:
            print('Errou! O número que você digitou é maior que o número'
                  ' secreto. Tente novamente.')
            print('Para sair digite "S".')
        elif numero_menor:
            print('Errou! O número que você digitou é menor que o número'
                  ' secreto. Tente novamente.')
            print('Para sair digite "S".')

        if n == 2:
            print('Última tentativas!\n')
        else:
            print(f'Você possuí {n + 1} tentativas.\n')
