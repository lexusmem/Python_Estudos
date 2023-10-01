class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'Código {self.codigo} Saldo {self.saldo}'


conta_alex = ContaCorrente(2)
conta_alex.deposita(1000)

conta_pamela = ContaCorrente(23)
conta_pamela.deposita(10000)


#  TUPLA & LISTA

#  podemos trabalhar com listas dentro de tuplas
alex = ('Alex', 37, 1987, 1000)  # tipo tupla
pamela = ('Pamela', 35, 1990, 2000)  # tipo tupla
print(f'Atributo "alex" {type(alex)}')
print(alex)
print(f'Atributo "pamela" {type(pamela)}')
print(pamela)
usuarios = [alex, pamela]  # tipo lista
print(f'Atributo "usuários" {type(usuarios)} que possuí objetos do tipo '
      f'{type(alex)}')
print(usuarios)
# posso add novos usuários pois o tipo do usuários é lista
# porem os dados dentro dos usuários são imutáveis
# pois são do tipo tupla
usuarios.append(('Laura', 7, 2012, 1000))
print(usuarios)


#  podemos trabalhar com tuplas dentro de listas
contas = (conta_alex, conta_pamela)
for conta in contas:
    print(conta)
contas[0].deposita(100)
for conta in contas:
    print(conta)
