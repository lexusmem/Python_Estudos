# Importação da função de calcular imposto de outro arquivo
from funcao_calcula_imposto import calcular_imposto_1

# Variáveis do tipo int são imutáveis
faturamento = 1500
print(faturamento)
faturamento = faturamento * 2

# Tupla são imutáveis
tvendas = (250, 320, 410)
# tvendas.append (1000)
# tvendas[0] = 367

# Lista são mutáveis
lvendas = [250, 320, 410]
lvendas[0] = 367
lvendas.append(1000)

print(tvendas, lvendas)

print(type(lvendas))
print(type(tvendas))


def calcular_imposto(preco, taxa):
    imposto = preco * taxa
    print(f"Preço: {preco} e Taxa {taxa}.")
    return imposto


# Argumentos informados de forma posicional
imposto = calcular_imposto(1500, 0.2)
print(imposto)

# Argumentos informados com as palavras chaves das funções com as Keywords
imposto = calcular_imposto(taxa=0.2, preco=1500)
print(imposto)

# Função criada com argumento opcional


def calcular_imposto_n(preco, taxa, outro_valor=None):
    imposto = preco * taxa
    print(f"Preço: {preco}, Taxa {taxa} e Outro Valor: {outro_valor}.")
    return imposto


# Argumentos opcional
imposto = calcular_imposto_n(1500, taxa=0.2)
print(imposto)

# Está parte utiliza a função importada de outro arquivo:
faturamento1 = 50000

ir = calcular_imposto_1(faturamento, 0.2)
iss = calcular_imposto_1(faturamento, 0.5)
csll = calcular_imposto_1(faturamento, 0.75)

print(ir, iss, csll)
