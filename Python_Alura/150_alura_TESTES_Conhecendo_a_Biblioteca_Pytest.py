from alura_testes import Usuarios, Lance, Leilao

alex = Usuarios('Alex')
laura = Usuarios('Laura')
pamela = Usuarios('Pamela')


lance_alex = Lance(alex, 200.00)
lance_laura = Lance(laura, 250.00)
lance_alex_2 = Lance(alex, 350.00)
lance_pamela = Lance(pamela, 1000.00)

leilao = Leilao('Celular')

leilao.propoe(lance_alex)
leilao.propoe(lance_laura)
leilao.propoe(lance_alex_2)
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

# Criado nova pasta e arquivo de teste.
