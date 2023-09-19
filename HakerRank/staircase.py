def staircase(n):
    valor = n
    for qtd in range(n):
        print(" "*(valor - 1), end="")
        print("#"*(qtd + 1))
        valor -= 1


staircase(6)
