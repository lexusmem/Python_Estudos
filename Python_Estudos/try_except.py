"""
Controle de exceção
"try" e "except
"""
try:
    a = {None}
    # print(a[1])
except NameError as erro:
    print('Variável não declarada. Erro: ', erro)
except (IndexError, KeyError) as erro:
    print('Erro de Índice ou Chave. Erro:', erro)
except Exception:
    print('Ocorreu um erro inesperado.')
else:
    # Else executa sempre que não ocorre erro no try
    print('Seu código foi executado com sucesso.')
    print(a)
finally:
    # Finally executa sempre independente de erro ou não.
    print('Finalmente')

print('Bora Continuar...')

try:
    numero = int(input('Digite um número: '))
except ZeroDivisionError:
    print('Está divisão por zero não é possível')
except ValueError:
    print('Digite apenas números.')
except NameError:
    print('Variável não declarada.')
except Exception as erro:
    print('Erro inesperado.', erro)
finally:
    # Finally executa sempre independente de erro ou não.
    print('Finalmente')
