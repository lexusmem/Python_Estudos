#  TUPLA
# Quando eu quero dar significado para cada posição
# elementos de tipos diferentes
# Representação com um conjunto de valores
# utilizamos a tupla

alex = ('Alex', 37, 1987, 1000)
pamela = ('Pamela', 35, 1990, 2000)
print(alex)
print(type(alex))
print(pamela)
print(type(pamela))

# variação 'funcional' (separando o comportamento dos dados)

conta_gui = (15, 1000)
print(conta_gui)

# tupla não é possível adicionar elementos e nem alterar.
# conta_gui.append(10)
# conta_gui[1] = 1100


def deposita(conta):
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    print(f'Deposito de R$ 100')
    return (codigo, novo_saldo)


# para alterar devo atribuir novo valor da tupla
deposita(conta_gui)
print(conta_gui)
conta_gui = deposita(conta_gui)
print(conta_gui)
