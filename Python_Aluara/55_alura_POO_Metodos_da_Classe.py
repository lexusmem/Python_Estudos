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

print(f'O limite da conta n° {conta_1.numero} é de {conta_1.limite:.2f}')
conta_1.limite = 2000

conta_1.extrato()
conta_1.sacar(5000)
conta_1.extrato()

print(Conta.codigo_banco())
bancos = (Conta.codigos_bancos())
print(bancos)
print(bancos['BB'])
print(bancos['Caixa'])
print(min(bancos.keys()), bancos['Bradesco'], list(bancos.keys())[0])


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

# Métodos Privados
# Para métodos em que sua utilização é restritas
# para outros métodos é necessário deixar o método
# privado para restringir a sua utilização dentro da classe
# utilizar "__" dois underscore igual é realizado nos atributos.

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

# Decoradores
# @property - substitui os get nos métodos
# @xxx.setter - substitui os set nos métodos

# Métodos da Classe
# Chamados de métodos estáticos.
# Métodos que retornam um valor independente de existir
# Um objeto instanciado.
# Utilizar o decorador no método:
# @staticmethod
