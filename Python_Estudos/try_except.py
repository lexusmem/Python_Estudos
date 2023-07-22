"""
Controle de exceção
"try" e "except
"""
try:
    a = {}
    # print(a[1])
except NameError as erro:
    print('Variável não declarada. Erro: ', erro)
except (IndexError, KeyError) as erro:
    print('Erro de Índice ou Chave. Erro:', erro)
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    # Else executa sempre que não ocorre erro no try
    print('Seu código foi executado com sucesso.')
    print(a)
finally:
    # Finally executa sempre independente de erro ou não.
    print('Finalmente')

print('Bora Continuar...')
