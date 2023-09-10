def jogar():

    print('=================================')
    print('===Bem vindo ao jogo de Forca!===')
    print('=================================')

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False

    # While - Enquanto
    while not enforcou and not acertou:
        print(f'Jogando ....{palavra_secreta}')

    print('=================================')
    print('===========Fim do Jogo===========')
    print('=================================')


if (__name__ == "__main__"):
    jogar()
