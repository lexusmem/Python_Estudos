# classe:
# filme

# objetos:
# nome
# ano
# duração
# likes

class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao


class Series:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas


vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
print(f'nome: {vingadores.nome}, Ano: {vingadores.ano}, '
      f'Duração: {vingadores.duracao}.')

atlanta = Series('Atlanta', 2018, 2)
print(f'nome: {atlanta.nome}, Ano: {atlanta.ano}, '
      f'Temporadas: {atlanta.temporadas}')
