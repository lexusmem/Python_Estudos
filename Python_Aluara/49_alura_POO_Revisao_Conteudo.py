from alura_POO_conta import Conta

# Criação do objeto através da classe Conta()
conta_1 = Conta(123, 'Alex', 55.5, 1000.00)
conta_2 = Conta(124, 'Sousa', 60, 1500.00)

print(conta_1)
print(conta_2)

# Acessando atributos dentro de um objeto
print(conta_1.titular)
print(conta_1.saldo)
print(conta_1.titular)
print(conta_2.saldo)

# Acessando métodos/funções dentro de um objeto
conta_1.extrato()
conta_1.deposita(15)
conta_1.extrato()
conta_1.sacar(5)
conta_1.extrato()

#  Foi falado na revisão sobre UML:

# Diagrama de Classe

# Criado uma Classe para criação de Objeto:
# class Conta

# Sobre os Atributos:
# self.numero = numero
# self.titular = titular
# self.saldo = saldo
# self.limite = limite

# Sobre os Métodos:
# extrato(self)
# deposita(self, valor)
# sacar(self, valor)
