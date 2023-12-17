from _43_alura_POO_dados_conta_teste import cria_conta
numero = 123
titular = 'Alex'
saldo = 55.00
limite = 1000.00

conta = {'numero': 123, 'titular': 'Alex',
         'Saldo': 55.00, 'limite': 1000.00}

conta2 = {'numero': 124, 'titular': 'Sousa',
          'Saldo': 20.00, 'limite': 500.00}

print(conta)
print(conta2)

print(conta['numero'])
print(type(conta))
print(type(conta['numero']))
print(type(conta['titular']))

conta3 = cria_conta(125, 'silva', 10.00, 2.00)

print(conta3)
