def breakingRecords(scores):
    valormaior = scores[0]
    valormenor = scores[0]
    maior = 0
    menor = 0
    for i, num in enumerate(scores):
        if i > 0:
            testemaior = num > valormaior
            if testemaior:
                valormaior = num
                maior += 1

            testemenor = num < valormenor
            if testemenor:
                valormenor = num
                menor += 1

    return maior, menor


teste = [12, 24, 10, 24]
print(breakingRecords(teste))
