def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular,
             'saldo': saldo, 'limite': limite}
    return conta


def depositar(conta, valor):
    conta['saldo'] += valor
    print(f"Deposito R$ {conta['saldo']:.2f}.")


def sacar(conta, valor):
    conta['saldo'] -= valor
    print(f"Saque R$ {conta['saldo']:.2f}.")


def extrato(conta):
    print(f"A conta {conta['numero']} possuí o saldo de {conta['saldo']:.2f}.")
