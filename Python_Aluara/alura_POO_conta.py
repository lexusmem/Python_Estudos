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
    # Função __init__ Função construtura
    # Dentro do Init construo os atributos
    # defino as características do objeto
    # Self é a referencia de construção do objeto.
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo Objeto...{self}")
        # Atributos:
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
