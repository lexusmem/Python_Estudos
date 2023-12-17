from alura_testes import Usuarios, Lance, Leilao

alex = Usuarios('Alex', 500.00)
laura = Usuarios('Laura', 500.00)
pamela = Usuarios('Pamela', 500.00)


leilao = Leilao('Celular')

alex.propoe_lance(leilao, 200.00)
laura.propoe_lance(leilao, 250.00)
pamela.propoe_lance(leilao, 300.00)


print(f'Lelião -> {leilao.descricao}.')
print(leilao.lances[0].usuario.nome)
print(f'O usuário {leilao.lances[0].usuario.nome} possuí na carteira '
      f'{leilao.lances[0].usuario.carteira:.2f}.')
print(f'{leilao.lances[0].valor:.2f}')
print(leilao.lances[1].usuario.nome)
print(f'O usuário {leilao.lances[1].usuario.nome} possuí na carteira '
      f'{leilao.lances[1].usuario.carteira:.2f}.')
print(f'{leilao.lances[1].valor:.2f}')
print(leilao.lances[2].usuario.nome)
print(f'O usuário {leilao.lances[2].usuario.nome} possuí na carteira '
      f'{leilao.lances[2].usuario.carteira:.2f}.')
print(f'{leilao.lances[2].valor:.2f}')

for lance in leilao.lances:
    print(f'No leilão {leilao.descricao} o usuário'
          f' {lance.usuario.nome} fez o lance de {lance.valor:.2f}.'
          f' E possuí na carteira {lance.usuario.carteira:.2f}.')

print(f'O menor lance foi de {leilao.menor_lance:.2f} e o maior lance foi de {
      leilao.maior_lance:.2f}.')

# Refaturamento dos métodos do arquivo principal "alura_testes"
