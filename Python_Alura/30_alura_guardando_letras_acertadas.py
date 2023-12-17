def jogar():

    print('=================================')
    print('===Bem vindo ao jogo de Forca!===')
    print('=================================')

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    palavra = str(" ".join(letras_acertadas))
    print(palavra)
    # While - Enquanto
    while not enforcou and not acertou:
        chute = input('Digite uma letra: ')
        chute = chute.strip()

        index = 0
        palavra_nao = 0

        for letra in palavra_secreta:

            if chute.upper() == letra.upper():
                letras_acertadas[index] = chute
                palavra = str(" ".join(letras_acertadas))
                palavra_nao += 1
            index += 1

        if palavra_nao == 0:
            print(f'A letra "{chute}" digitada não encontrada na Forca.')

        print(palavra)

    print('=================================')
    print('===========Fim do Jogo===========')
    print('=================================')


if (__name__ == "__main__"):
    jogar()
