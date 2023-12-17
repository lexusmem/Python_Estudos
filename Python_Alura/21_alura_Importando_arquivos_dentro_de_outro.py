import alura_jogo_adivinhacao
import alura_jogo_forca

print('=================================')
print('=======Escolha o Seu Jogo========')
print('=================================')

print('(1) Forca (2) Adivinhação')

jogo = int(input("Qual o Jogo? "))

if jogo == 1:
    print("Jogando forca")
    alura_jogo_forca.jogar()

elif jogo == 2:
    print("Jogando Adivinhação")
    alura_jogo_adivinhacao.jogar()
