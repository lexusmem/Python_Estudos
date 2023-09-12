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
        chute = chute.strip()

        index = 0
        palavra_nao = 0

        # list - transforma uma string em lista
        # palavra_lista = list(palavra_secreta.upper())
        # consultar se algum dado consta na lista "b" in palavra_secreta
        # acessar valor de uma lista posição palavra_lista[0]
        # tamanho de uma lista
        # saber que valor minimo e maximo dentro de uma lista
        # min(palavra_lista) e max(palavra_lista)
        # tamanho de uma lista len(palavra_lista)
        # add valor na lista palavra_lista.append("1")
        # remover ultimo valor palavra_lista.pop()

        for letra in palavra_secreta:

            if chute.upper() == letra.upper():
                print(f'Encontrei a letra "{chute}" na posição "{index}".')
                palavra_nao += 1
            index += 1

        if palavra_nao == 0:
            print(f'A letra "{chute}" digitada não encontrada na Forca.')
        print(f'Jogando chute: {chute} - palavra secreta: {palavra_secreta}.')

    print('=================================')
    print('===========Fim do Jogo===========')
    print('=================================')


if (__name__ == "__main__"):
    jogar()
