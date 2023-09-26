# classe:
# filme

# objetos:
# nome
# ano
# duração
# likes

# Classe Mãe:
# class Programa

# Classes Filhos:
# class Filme(Programa)
# class Series(Programa)

# Nas classes filhos chamamos a classe mae
# através do "super()". Exemplo:
# super().__init__(nome, ano)

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
        super().__init__(nome, ano)
        self.duracao = duracao

    # É possível criar métodos exclusivos para as classes filhos
    # Exemplo:
    def exemplo_metodo_exclusivo(self):
        pass


class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


# Instanciando as classes
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Series('atlanta', 2018, 2)

vingadores.dar_likes()
atlanta.dar_likes()

print(f'Nome: {vingadores.nome}, Ano: {vingadores.ano}, '
      f'Duração: {vingadores.duracao} min., Likes: {vingadores.likes}.')

print(f'Nome: {atlanta.nome}, Ano: {atlanta.ano}, '
      f'Temporadas: {atlanta.temporadas}, Likes: {atlanta.likes}')
