# Operadores
# Soma +
# Divisão Inteira //
# Resto da divisão %

# Faça um programa para loja de tintas
# Solicitar tamanho da area em metros quadrados area a ser pitnada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# Tinta vendida em latas de 18 litros
# Cada lata custa R$ 80
# Informar quantidade de latas de tintas a serem compradas, quantidade de
# sobra e o preço total

altura = float(input('Informe a altura: '))
largura = float(input('Informe a largura: '))

metro_quadrado = altura * largura

print(f'O metro quadrado calculado é de {metro_quadrado: .2f}.')

qtd_tinta = metro_quadrado / 3

qtd_tinta_inteiro = metro_quadrado // 3

print(qtd_tinta)
print(qtd_tinta_inteiro)
