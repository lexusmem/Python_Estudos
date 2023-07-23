def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as erro:
        print('Log: ', erro)
    # Função raise permite que o erro e nova except
    # seja utilizado fora desta função
    # e conste o erro em todas as execução do erro
        raise


try:
    print(divide(n1=2, n2=0))
except ZeroDivisionError as erro:
    print(erro)

# Criando nossa própria mensagem de erro
print('===Mensagem de Erro Customizada===')


def divide2(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')
    return n1/n2


try:
    print(divide2(n1=2, n2=0))
except ValueError as error:
    print(error)
