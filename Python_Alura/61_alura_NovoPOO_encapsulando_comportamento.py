# classe:
# filme

# objetos:
# nome
# ano
# duração
# likes

class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1


class Series:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

print(f'Nome: {vingadores.nome}, Ano: {vingadores.ano}, '
      f'Duração: {vingadores.duracao}, Likes: {vingadores.likes}.')

atlanta = Series('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()

print(f'Nome: {atlanta.nome}, Ano: {atlanta.ano}, '
      f'Temporadas: {atlanta.temporadas}, Likes: {atlanta.likes}')
