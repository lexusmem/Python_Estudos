# pedir o tamanho em metros quadrados
# cobertura da tinta é de 1 litro para cada 3 metros quadrados
# vendida em latas de 18 litros
# cada lata custa $80
# Informar a quantidade de latas necessarias e valor total
# Informar a quantidade de tinta que ira sobrar

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

metro2 = largura * altura

print(f'A parede tem um total de{metro2: .2f} m².')

qtd_tinta = metro2 / 3

if qtd_tinta == round(qtd_tinta):
    litros = qtd_tinta
else:
    litros = round(qtd_tinta+0.5)

print(f'É preciso {litros} lt de tinta para pintar a parede.')

latas = litros / 18

if latas == round(latas):
    qtd_latas = latas
else:
    qtd_latas = round(latas+0.5)

print(f'É preciso {qtd_latas} latas de tintas.')

valor = qtd_latas * 80

texto_valor = f'R$ {valor:_.2f}'
texto_valor = texto_valor.replace('.', ',').replace('_', '.')

print(f'Será gasto um total de {texto_valor}.')
