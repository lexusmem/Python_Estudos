frutas = ["abacate", "abacaxi", "acerola", "amora", "banana", "cereja", "figo",
          "goiaba", "graviola", "kiwi", "laranja", "limão", "mamão", "manga",
          "melancia"]

arquivo = open('palavras.txt', 'w')

for fruta in frutas:
    arquivo.write(fruta + '\n')

arquivo.close()
