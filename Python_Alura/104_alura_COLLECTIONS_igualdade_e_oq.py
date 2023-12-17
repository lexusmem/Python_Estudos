class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'Código {self._codigo} Saldo {self._saldo}'


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    # definindo método de condição de igualdade
    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo

    def deposito(self, valor):
        self._saldo += valor
        print(f'Deposito de R$ {valor:.2f} na conta {self._codigo}.')

    def __str__(self):
        return f'Conta Número {self._codigo} Saldo R$ {self._saldo:.2f}.'


class ContaMultiploSalario(ContaSalario):
    pass


alex_salario = ContaSalario(1)
print(alex_salario)
alex_salario.deposito(100)
print(alex_salario)
print(id(alex_salario))

alex_salario_1 = ContaSalario(1)
print(alex_salario_1)
alex_salario_1.deposito(100)
print(alex_salario_1)
print(id(alex_salario_1))

alex_multiplo = ContaMultiploSalario(2)

alex_corrente = ContaCorrente(1)
alex_corrente.deposita(1000)


# tem o mesmos valores atribuídos
# Mas são objetos diferentes

# para verificar a igual através de um determinado
# atributo criar método __eq__ para comparar o numero do codigo
print('Comparação == __eq__ código:')
print(alex_salario == alex_salario_1)
print('Comparação != __eq__ código:')
print(alex_salario != alex_salario_1)

# comparando se os objetos são instancias
# de alguma classe
print("Comparativo se são classes das instâncias:")
print(isinstance(alex_salario, ContaSalario))
print(isinstance(alex_salario, ContaSalario))
print(isinstance(alex_multiplo, ContaSalario))
print(isinstance(alex_corrente, Conta))
print(isinstance(alex_corrente, ContaPupanca))
