# classe:
# filme

# objetos:
# nome
# ano
# duração
# likes

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0


class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0


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
