# classe:
# filme

# objetos:
# nome
# ano
# duração
# likes

class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_likes(self):
        self.likes += 1


class Series:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_likes(self):
        self.likes += 1


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

print(f'nome: {vingadores.nome}, Ano: {vingadores.ano}, '
      f'Duração: {vingadores.duracao}, Likes: {vingadores.likes}.')

atlanta = Series('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()

print(f'nome: {atlanta.nome}, Ano: {atlanta.ano}, '
      f'Temporadas: {atlanta.temporadas}, Likes: {atlanta.likes}')
