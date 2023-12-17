from alura_testes import Usuarios, Lance, Leilao

alex = Usuarios('Alex')
laura = Usuarios('Laura')
pamela = Usuarios('Pamela')


lance_laura = Lance(laura, 300.00)
lance_alex = Lance(alex, 200.00)
lance_pamela = Lance(pamela, 1000.00)

leilao = Leilao('Celular')

leilao.propoe(lance_alex)
leilao.propoe(lance_laura)
leilao.propoe(lance_pamela)

print(leilao.descricao)
print(leilao.lances[0].usuario.nome)
print(f'{leilao.lances[0].valor:.2f}')
print(leilao.lances[1].usuario.nome)
print(f'{leilao.lances[1].valor:.2f}')
print(leilao.lances[2].usuario.nome)
print(f'{leilao.lances[2].valor:.2f}')

for lance in leilao.lances:
    print(f'No leilão {leilao.descricao} o usuário'
          f' {lance.usuario.nome} fez o lance de {lance.valor:.2f}.')

print(f'O menor lance foi de {leilao.menor_lance:.2f} e o maior lance foi de {
      leilao.maior_lance:.2f}.')

# Criado arquivo alura_avaliador_test para realizações dos testes
# Novo teste no arquivo alura_avaliador_test para realizações dos testes
# Teste realizado no menor e maior lance, se a Classe Avaliado esta correta.
# Renomeado as funções de testes para entendimento do que esta sendo testado.
# Criado dois testes para validar quando existir um único lance
# e quando existir mais de dois lances.
# Isolar os objetos para melhorar o código de teste.
# Criando o método SetUp com criação das classes que serão
# utilizadas em todos os testes
# Incluído método "propoe" que propõe o encapsulamento
# para os lances ao leilões realizado pelos usuários.
# Aula sobre a necessidade de existir uma classe avaliador com seus métodos
# Ou incluir os métodos de avaliação estar na classe Leilão
# Implementação de novas regras:
# Um lance de cada vez.
# E lance maior que o anterior.
