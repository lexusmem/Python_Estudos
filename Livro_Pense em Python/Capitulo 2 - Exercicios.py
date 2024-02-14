import math

# Calcule o volume de uma esfera com o raio r igual a 5:
r = 5
volume = 4/3 * math.pi * r**3
print(volume)

# Suponha que o preço de capa de um livro seja 24.95
# mas as livrarias recebem um desc de 40%
# O transporte custa 3 para o primeiro exemplar e 75 cents para os demais
# Qual o custo para 60 cópias?
desc = (1-(40/100))
valor_livro = 24.95 * desc
valor_total_livro = 60 * valor_livro
valor_transporte = 59 * 0.75 + 3
valor_total = valor_total_livro + valor_transporte
print(f'{valor_total:.2f}')


# Somar horas
# Se eu sair de casa 6:52 e correr
# 1km a 8min15s
# 3km a 7min12s
# 1km a 8min15s
# que horas chego?
def somar_tempo(hora1, hora2, hora3, hora4):
    segundos_totais1 = hora1[0] * 3600 + hora1[1] * 60 + hora1[2]
    segundos_totais2 = hora2[0] * 3600 + hora2[1] * 60 + hora2[2]
    segundos_totais3 = hora3[0] * 3600 + hora3[1] * 60 + hora3[2]
    segundos_totais4 = hora4[0] * 3600 + hora4[1] * 60 + hora4[2]

    soma_segundos = segundos_totais1 + \
        (segundos_totais2 * 3) + segundos_totais3 + segundos_totais4

    horas = soma_segundos // 3600
    minutos = (soma_segundos % 3600) // 60
    segundos = soma_segundos % 60

    return horas, minutos, segundos


hora1 = (0, 8, 15)
hora2 = (0, 7, 12)
hora3 = (0, 8, 15)
hora4 = (6, 52, 0)
soma_tempo = somar_tempo(hora1, hora2, hora3, hora4)
print(f"Soma das horas: {soma_tempo[0]}:{soma_tempo[1]}:{soma_tempo[2]}")
