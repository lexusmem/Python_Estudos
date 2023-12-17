class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    # def get_nome(self):
    #     return self.nome.title()

    # Get - Outra forma de fazer:
    @property
    def nome(self):
        print('Chamando @property nome() "Get"')
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print('Chamando @setter nome()')
        self.__nome = nome
