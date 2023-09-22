from alura_POO_conta import Conta

# Criação do objeto através da classe Conta()
conta_1 = Conta(123, 'Alex', 55.5, 1000.00)
conta_2 = Conta(124, 'Sousa', 60, 1500.00)

print(conta_1)
print(conta_2)

# Acessando métodos/funções dentro de um objeto
conta_1.extrato()
conta_1.deposita(15)
conta_1.extrato()
conta_1.sacar(5)
conta_1.extrato()

valor = 10
conta_1.transferencia(valor, conta_2)
conta_1.extrato()
conta_2.extrato()

# Acessando atributos dentro de um objeto
# Como os atributos estão privados não é possível acessar direto
# Somente através do métodos.
# print(conta_1.__titular)
# print(conta_1.__saldo)
# print(conta_1.__titular)
# print(conta_2.__saldo)

# conta_1.__saldo = 20
# Não é possível atribuir um valor direto em
# um atributo privado.

#  Foi falado na revisão sobre UML:

# Diagrama de Classe

# Criado uma Classe para criação de Objeto:
# class Conta

# Sobre os Atributos:
# self.numero = numero
# self.titular = titular
# self.saldo = saldo
# self.limite = limite

# Para criação de atributos privados
# Inserir "__" na frente do atributo
# Com isso não pode ser mais acessado diretamente
# somente através do métodos

# Sobre os Métodos:
# extrato(self)
# deposita(self, valor)
# sacar(self, valor)

# Garbage collector (coletor de lixo).
# Para objetos em que não esta mais sendo utilizado (projetos abandonados),
# o python limpa este espaço em memoria para ser.
# reutilizado.
# Exemplo:
# conta_1 = Conta(123, 'Alex', 55.5, 1000.00)
# conta_1 = Conta(123, 'Alex', 55.5, 1000.00)
# criação de dois objetos com a mesma variável,
# onde o primeiro não possui mais o vinculo da
# variável não podendo ser mais localizado.

# None
# conta_1 = Conta(123, 'Alex', 55.5, 1000.00)
# nova_variável = conta_1
# nova_variável apontando para o mesmo objeto da
# variável conta_1 (não criou um novo objeto)
# Para De-Referencia esta nova_variável é somente
# atribuir a ela None
# nova_variável = None
