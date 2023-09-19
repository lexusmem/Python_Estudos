import random


def jogar():

    mensagem_abertura()

    palavra_secreta = carrega_palavras_secretas()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    palavra = str(" ".join(letras_acertadas))
    print(palavra)

    enforcou = False
    acertou = False
    erros = 0

    # While - Enquanto
    while not enforcou and not acertou:
        chute = pede_chute()
        index = 0
        palavra_nao = 0

        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = chute
                palavra = str(" ".join(letras_acertadas))
                palavra_nao += 1
            index += 1

        if palavra_nao == 0:
            desenha_forca(erros, chute)
            erros += 1
            if erros >= 7:
                imprime_mensagem_perdedor(palavra_secreta)
                break

        print(palavra)
        if "_" not in palavra:
            imprime_mensagem_vencedor()
            acertou = True

    mensagem_fechamento()


def mensagem_abertura():
    print('=================================')
    print('===Bem vindo ao jogo de Forca!===')
    print('=================================')


def mensagem_fechamento():
    print('=================================')
    print('===========Fim do Jogo===========')
    print('=================================')


def carrega_palavras_secretas():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]


def pede_chute():
    chute = input('Digite uma letra: ')
    chute = chute.strip()
    return chute


def desenha_forca(erros, chute):
    print(f'\nA letra "{chute}" digitada não encontrada na Forca.')
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()  # desenho da forca.


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")  # desenho do troféu
    print("\n")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")  # desenho da caveira


if (__name__ == "__main__"):
    jogar()
