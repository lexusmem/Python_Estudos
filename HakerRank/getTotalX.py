def getTotalX(a, b):
    maior = max(b)

    lista_b1 = []
    tamb = len(b)

    for item_b in range(tamb):
        for x in range(1, b[item_b]+1):
            if b[item_b] % x == 0:
                lista_b1.append(x)

    tabuada_a = []
    tama = len(a)

    for item_a in range(tama):
        contador = 1
        resultado = 0
        while resultado < maior:
            resultado = a[item_a] * contador
            tabuada_a.append(resultado)
            contador += 1

    nums = (tabuada_a + lista_b1)

    dup = {x for x in nums if nums.count(x) >= len(a)+len(b)}

    return int(len(dup))


a = [2, 4]
b = [16, 32, 96]

a = getTotalX(a, b)
print(a)
