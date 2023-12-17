from _44_alura_POO_dados_comportamento import cria_conta, depositar
from _44_alura_POO_dados_comportamento import sacar, extrato

conta = cria_conta(125, 'silva', 10.00, 2.00)
extrato(conta)
depositar(conta, 200)
extrato(conta)
sacar(conta, 10.)
extrato(conta)
