import random

print('=================================')
print('Bem vindo ao jogo de adivinhação!')
print('=================================')

numero_secreto = random.randrange(1, 101)
# numero_secreto = int(round(random.random() * 100))

# print(numero_secreto)
tentativas = 0

print("Qual o nível de dificuldade")
print("(1)Fácil (2)Médio (3)Difícil")

nivel = int(input("Defina o nível: "))

if nivel == 1:
    tentativas = 20
    print(
        f"Nível de dificuldade selecionada ({nivel})Fácil {tentativas}"
        " tentativas.")
elif nivel == 2:
    tentativas = 10
    print(
        f"Nível de dificuldade selecionada ({nivel})Médio {tentativas}"
        " tentativas.")
elif nivel == 3:
    tentativas = 5
    print(
        f'Nível de dificuldade selecionada ({nivel})Difícil {tentativas}'
        'tentativas.')

for n in range(1, tentativas + 1):

    numero_usuario = input('Digite o número secreto entre 1 e 100: ')

    sair = numero_usuario.capitalize() == 'S'

    if sair:
        print('Sair.')

    if not numero_usuario.isnumeric():
        if n > tentativas:
            print('Você perdeu!')
            continue
        if n >= tentativas:
            print('Valor Inválido. Digite um número.')
            print('Última tentativas!\n')
        else:
            print('Valor Inválido. Digite um número.')
            print(f'Você possuí {tentativas - n} tentativas.\n')

        continue

    if int(numero_usuario) < 1 or int(numero_usuario) > 100:
        if n > tentativas:
            print('Você perdeu!')
            continue
        if n == tentativas:
            print("Digite um número entre 1 e 100.")
            print('Última tentativas!\n')
        else:
            print("Digite um número entre 1 e 100.")
            print(f'Você possuí {tentativas - n} tentativas.\n')

        continue

    acertou = int(numero_usuario) == numero_secreto
    numero_maior = int(numero_usuario) > numero_secreto
    numero_menor = int(numero_usuario) < numero_secreto

    if acertou:
        print('Você acertou!\n'
              '====Fim de Jogo====')
        break
    else:
        if n == tentativas:
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

        if n == tentativas - 1:
            print('Última tentativas!\n')
        else:
            print(f'Você possuí {tentativas - n} tentativas.\n')
