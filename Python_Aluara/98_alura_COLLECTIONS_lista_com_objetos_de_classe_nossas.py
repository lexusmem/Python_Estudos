class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'Código {self.codigo} Saldo {self.saldo}'


conta_alex = ContaCorrente(2)
print(conta_alex)

conta_alex.deposita(1000)
print(conta_alex)

conta_pamela = ContaCorrente(23)
conta_pamela.deposita(10000)
print(conta_pamela)

contas = [conta_alex, conta_pamela]
print(contas)
for conta in contas:
    print(conta)
print(id(contas[0]))
print(id(conta_alex))
