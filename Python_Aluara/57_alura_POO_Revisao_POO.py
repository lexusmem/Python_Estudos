# Classe:
# Conta() - Objeto
# Função __init__ Função construtura Classe
# Exemplo de um método de construção:
# def __init__(self, numero, titular, saldo, limite):

# Atributos da Classe - Objeto:
# self.numero
# self.titular
# self.saldo
# self.limite

# Métodos:
# extrato(self)
# deposita(self, valor)
# saca(self)
# transfere(self, valor, conta_transferido)

# # Privados
# Os métodos e os atributos podem ser privados
# Com python para tornar privados utilizamos "__"
# Exemplo:
# atributos privados:
# self.__numero
# métodos privados:
# __pode_sacar(self, valor_a_sacar)

# Get - @property
# Para evitar acessar os atributos diretamente
# Quando precisamos buscar um valor utilizamos o método get
# podemos utilizar o método get, exemplo:
# def get_saldo(self)
# Ou através do decorador @property, exemplo:
# @property
# def saldo(self)

# Quando precisamos atribuir um valor utilizamos o método setter
# podemos utilizar o método set, exemplo:
# def set_limite(self, valor)
# Ou através do decorador @setter, exemplo:
# @limite.setter
# def limite(self, valor)

# Para métodos de classes pode ser atribuído o decorador
# @staticmethod, exemplo:
# @staticmethod
# def codigos_bancos():
