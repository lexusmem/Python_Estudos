def birthdayCakeCandles(candles):
    maior = max(candles)
    contagem = 0

    for num in candles:
        if num == maior:
            contagem += 1

    return contagem


velas = [3, 2, 1, 3]

print(birthdayCakeCandles(velas))
