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
# tupla não é possível adicionar elementos e nem alterar.
# alex.append(10)
# alex[3] = 1100
def deposita(conta, valor):
    nome = conta[0]
    idade = conta[1]
    ano = conta[2]
    novo_saldo = conta[3] + valor
    print('Deposito de R$ 100')
    return (nome, idade, ano, novo_saldo)


# para alterar devo atribuir novo valor da tupla
deposita(alex, 200)
print(alex)
alex = deposita(alex, 300)
print(alex)

deposita(pamela, 200)
print(alex)
alex = deposita(alex, 500)
print(alex)
