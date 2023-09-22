# POO
# Classe é uma estrutura de programação que descreve as características
# e comportamentos de um objeto.

'''
Objetos
A orientação a objetos visa representar, de maneira idêntica, as situações
do mundo real nos sistemas computacionais. Para ela, os sistemas operacionais
não devem ser vistos como uma coleção estruturada de processos,
mas sim como uma coleção de objetos que interagem uns com os
outros organizadamente, assim como ocorre no mundo real.

Em uma concepção abrangente, um objeto pode ser entendido como sendo um
elemento físico, por exemplo, uma pedra, uma cadeira ou um animal,
ou como um elemento abstrato, como uma conta bancária.
'''


class Conta:
    # Função __init__ Função construtura Classe
    # Dentro do Init construo os atributos
    # defino as características do objeto
    # E crio os métodos/funções da minha classe
    # Self é a referencia de construção do objeto.
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo Objeto...{self}")
        # Atributos:
        # Atributos Privados "__":
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Métodos - Criação de métodos/funções que consta no objeto:
    def extrato(self):
        print(
            f'Saldo de {self.saldo:.2f} na conta do '
            f'titular {self.titular}.')

    def deposita(self, valor):
        self.__saldo += valor
        print(f'Deposito de {valor:.2f} na conta do titular {self.titular}.')

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print(f'Saque de -{valor:.2f} na conta do titular {self.titular}.')
        else:
            print(
                f'O valor de saque ultrapassa o seu limite atual de '
                f'{self.saldo + self.limite:.2f}')

    def transferencia(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)
        print(
            f'Transferência realizada R$ {valor} de {self.titular} para '
            f'{destino.titular}.')

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        print(
            f'Atribuído novo limite de {self.limite:.2f} a conta '
            f'{self.numero}.')

    @property
    def numero(self):
        return self.__numero

# Para criação de atributos privados
# Inserir "__" na frente do atributo
# Com isso não pode ser mais acessado diretamente
# somente através do métodos
