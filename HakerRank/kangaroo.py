def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1:
        return "NO"
    else:
        if (x1 != x2) and (v1 != v2) and (x2 - x1) % (v1 - v2) == 0:
            return "YES"
        else:
            return "NO"


teste = kangaroo(2, 1, 1, 2)
print(teste)

teste1 = kangaroo(14, 4, 98, 2)
print(teste1)

teste3 = kangaroo(43, 2, 70, 2)
print(teste3)
