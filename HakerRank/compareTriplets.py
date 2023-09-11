def compareTriplets(a, b):

    alicia = 0
    breno = 0
    i = 0

    while i < len(a):
        if a[i] > b[i]:
            alicia += 1
        elif a[i] < b[i]:
            breno += 1
        i += 1
    resultado = [alicia, breno]

    return resultado


print(compareTriplets([5, 6, 7], [3, 6, 10]))
