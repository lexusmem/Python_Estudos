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

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - {self._likes} Likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # É possível criar métodos exclusivos para as classes filhos
    # Exemplo:
    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duração: '\
            f'{self.duracao} min. - {self._likes} Likes'


class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} '\
            f'Temporadas: {self.temporadas} - {self._likes} Likes'


class Playlist:
    def __init__(self, nome_da_playlist, programas):
        self.nome_da_playlist = nome_da_playlist
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)


# Instanciando as classes
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Series('atlanta', 2018, 2)
tmp_1 = Filme('Todo mundo em pânico', 2000, 88)
suits = Series('Suits', 2011, 9)

vingadores.dar_likes()
atlanta.dar_likes()
tmp_1.dar_likes()
tmp_1.dar_likes()
suits.dar_likes()
suits.dar_likes()
suits.dar_likes()
suits.dar_likes()


# ↓↓↓↓↓↓↓ Polimorfismo ↓↓↓↓↓↓↓

filmes_e_series = [vingadores, atlanta, tmp_1, suits]
print('Filmes e Series criadas na classe Programas!')
for programa in filmes_e_series:
    print(programa)

print('\nPlaylist Fim de Semana!')
playlist_fim_de_semana = Playlist('Fim de semana', [suits, tmp_1])
print(
    f'Tamanho da playlist: {playlist_fim_de_semana.tamanho} programas.')
for programa in playlist_fim_de_semana.listagem:
    print(programa)
print(f'{atlanta.nome} está na playlist? '
      f'{atlanta in playlist_fim_de_semana.listagem}.')
