def jogar():

    print('=================================')
    print('===Bem vindo ao jogo de Forca!===')
    print('=================================')

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False

    # While - Enquanto
    while not enforcou and not acertou:
        chute = input('Digite uma letra: ')

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                print(f'Encontrei a letra "{chute}" na posição "{index}"')
            index += 1
        print(f'Jogando chute: {chute}....palavra secreta: {palavra_secreta}')

    print('=================================')
    print('===========Fim do Jogo===========')
    print('=================================')


if (__name__ == "__main__"):
    jogar()
