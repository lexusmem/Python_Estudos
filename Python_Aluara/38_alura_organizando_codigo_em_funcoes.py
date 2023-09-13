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


def mensagem_abertura():
    print('=================================')
    print('===Bem vindo ao jogo de Forca!===')
    print('=================================')


def carrega_palavras_secretas():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    # print(palavras[numero])
    palavra_secreta = palavras[numero]
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]


if (__name__ == "__main__"):
    jogar()
