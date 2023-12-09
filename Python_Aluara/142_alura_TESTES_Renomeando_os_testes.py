from alura_testes import Avaliador, Usuarios, Lance, Leilao

alex = Usuarios('Alex')
laura = Usuarios('Laura')

lance_laura = Lance(laura, 300.00)
lance_alex = Lance(alex, 200.00)

leilao = Leilao('Celular')

leilao.lances.append(lance_alex)
leilao.lances.append(lance_laura)

print(leilao.descricao)
print(leilao.lances[0].usuario.nome)
print(f'{leilao.lances[0].valor:.2f}')
print(leilao.lances[1].usuario.nome)
print(f'{leilao.lances[1].valor:.2f}')

for lance in leilao.lances:
    print(f'No leilão {leilao.descricao} o usuário'
          f' {lance.usuario.nome} fez o lance de {lance.valor:.2f}.')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {
      avaliador.maior_lance}.')

# Criado arquivo alura_avaliador_test para realizações dos testes
# Novo teste no arquivo alura_avaliador_test para realizações dos testes
# Teste realizado no menor e maior lance, se a Classe Avaliado esta correta.
# Renomeado as funções de testes para entendimento do que esta sendo testado.
