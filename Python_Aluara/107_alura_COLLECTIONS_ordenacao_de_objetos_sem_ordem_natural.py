from operator import attrgetter
idades = [34, 54, 67, 77, 89, 45]

nomes = ['alex', 'pamela', 'laura', 'bryan', 'gabriel']

print(sorted(nomes))


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


alex_salario = ContaSalario(1)
alex_salario.deposito(200)

pamela_salario = ContaSalario(3)
pamela_salario.deposito(200)

laura_salario = ContaSalario(4)
laura_salario.deposito(200.01)

gabriel_salario = ContaSalario(2)
gabriel_salario.deposito(50.72)

contas = [alex_salario, pamela_salario, laura_salario, gabriel_salario]


print('impressão por ordem de saldo da conta')


def extrai_saldo(conta):
    return conta._saldo


for conta in sorted(contas, key=extrai_saldo, reverse=True):
    print(conta)


print('impressão por ordem de codigo da conta')


def extrai_codigo(conta):
    return conta._codigo


for conta in sorted(contas, key=extrai_codigo):
    print(conta)

# utilizando o modulo operator
# função attrgetter
print('impressão por ordem de codigo da conta com attrgetter')
for conta in sorted(contas, key=attrgetter("_codigo")):
    print(conta)

# posso utilizar um segundo atributo para o filtro
print('impressão por ordem de saldo e codigo da conta com attrgetter')
for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
    print(conta)
