from functools import total_ordering


# Definido o método de comparação de igualdade __eq__
# o método de comparação menor __lt__
# importado o método total_ordering para comparação
# de menor igual ou maior igual

@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    # definindo método de condição de igualdade
    # para comparar classes instancias das classes possuem
    # o mesmo código sendo assim a mesma conta
    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo

    # definindo método de para verificar qual saldo é maior
    # para ordenar as contas pelo valor do saldo
    # e depois pelo número do código
    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def deposito(self, valor):
        self._saldo += valor
        print(f'Deposito de R$ {valor:.2f} na conta {self._codigo}.')

    def __str__(self):
        return f'Conta Número {self._codigo} Saldo R$ {self._saldo:.2f}.'


alex_salario = ContaSalario(1)
alex_salario.deposito(200)

pamela_salario = ContaSalario(3)
pamela_salario.deposito(200)

laura_salario = ContaSalario(4)
laura_salario.deposito(200.01)

gabriel_salario = ContaSalario(2)
gabriel_salario.deposito(50.72)

contas = [alex_salario, pamela_salario, laura_salario, gabriel_salario]

for conta in sorted(contas):
    print(conta)

comparacao = pamela_salario <= laura_salario

print(comparacao)
