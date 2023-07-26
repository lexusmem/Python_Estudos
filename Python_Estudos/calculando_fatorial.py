# https://youtu.be/SJsg5Y6c7_A

def main():
    n = int(input('Digite o valor de n!: '))
    resp = fatorial(n)
    print(f'O valor de {n}! é igual à {resp}.')


def fatorial(n):
    # calcular fatorial
    fat = 1
    for i in range(2, n+1):
        fat = fat * i
    return fat


main()
