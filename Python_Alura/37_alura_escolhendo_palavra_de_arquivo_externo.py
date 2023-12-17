import random


def jogar():

    print('=================================')
    print('===Bem vindo ao jogo de Forca!===')
    print('=================================')

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    # print(palavras[numero])
    palavra_secreta = palavras[numero]

    enforcou = False
    acertou = False
    letras_acertadas = ['_' for letra in palavra_secreta]

    # for letra in palavra_secreta:
    #     letras_acertadas.append('_')

    erros = 0

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
            erros += 1
            if erros >= len(palavra_secreta):
                print("\nVocê não conseguiu acertar a palavra secreta.\n")
                break

        print(palavra)
        if "_" not in palavra:
            print('Você acertou a Palavra Secreta!')
            acertou = True

    print('=================================')
    print('===========Fim do Jogo===========')
    print('=================================')


if (__name__ == "__main__"):
    jogar()
