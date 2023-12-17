from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'Código {self._codigo} Saldo {self._saldo}'

    @abstractmethod
    def passa_o_mes(self):
        pass


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):
    pass


conta_alex = ContaCorrente(1)
conta_alex.deposita(1000)

conta_pamela = ContaPupanca(2)
conta_pamela.deposita(1000)

# ↓↓↓↓↓↓↓POLIMORFISMO↓↓↓↓↓↓↓
contas = [conta_alex, conta_pamela]
for conta in contas:
    conta.passa_o_mes()  # duck typing
    print(conta)
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

containvestimento = ContaInvestimento(3)
print(containvestimento)
