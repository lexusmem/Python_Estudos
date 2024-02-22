def right_justify(s):
    qtd_palavra = len(s)
    espacos = ' ' * (70-qtd_palavra)
    print(espacos, s, sep="")
    return qtd_palavra + len(espacos)


right_justify('alex')
right_justify('monty')
right_justify('python')


def do_twice(f, valor):
    f(valor)
    f(valor)


def print_spam(x):
    print(x)


do_twice(print_spam, 'teste')


def print_twice(alex):
    print(alex)
    print(alex)


do_twice(print_twice, 'spam')


def do_four(f, valor):
    do_twice(f, valor)
    do_twice(f, valor)


do_four(print_spam, 'quatro')


def separador():
    print('+', end=' ')
    print('- ' * 4, end='')
    print('+', end=' ')
    print('- ' * 4, end='')
    print('+')


def separador_2():
    print('+', end=' ')
    print('- ' * 4, end='')
    print('+', end=' ')
    print('- ' * 4, end='')
    print('+', end=' ')
    print('- ' * 4, end='')
    print('+', end=' ')
    print('- ' * 4, end='')
    print('+')


def linha():
    print('|', ' ' * 7, '|', ' ' * 7, '|')
    print('|', ' ' * 7, '|', ' ' * 7, '|')
    print('|', ' ' * 7, '|', ' ' * 7, '|')
    print('|', ' ' * 7, '|', ' ' * 7, '|')


def linha_2():
    print('|', ' ' * 7, '|', ' ' * 7, '|', ' ' * 7, '|', ' ' * 7, '|')
    print('|', ' ' * 7, '|', ' ' * 7, '|', ' ' * 7, '|', ' ' * 7, '|')
    print('|', ' ' * 7, '|', ' ' * 7, '|', ' ' * 7, '|', ' ' * 7, '|')
    print('|', ' ' * 7, '|', ' ' * 7, '|', ' ' * 7, '|', ' ' * 7, '|')


def duas_colunas():
    separador()
    linha()
    separador()
    linha()
    separador()


def quatro_colunas():
    separador_2()
    linha_2()
    separador_2()
    linha_2()
    separador_2()
    linha_2()
    separador_2()
    linha_2()
    separador_2()


duas_colunas()
print('\n \n')
quatro_colunas()
