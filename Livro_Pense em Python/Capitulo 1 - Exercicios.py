# 1 - Em uma instrução print o que acontece se esquecer
# um parenteses ou ambos?

print('Teste de Erro')

# Resposta: Erro de sintaxe
# SyntaxError: '(' was never closed
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

# 2 - Se estiver tentando imprimir uma string, o que acontece se omitir
# uma das aspas ou ambas?

print('Teste erro')

# Resposta: Erro de sintaxe
# SyntaxError: unterminated string literal
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

# 3 - Você pode usar um sinal de menos para fazer um número negativo
# como -2. O que acontece se puser um sinal de mais antes de um número?
# E escrever assim 2 + + 2?

numero_negativo = -2
print(2 + + 2)

# Resposta = Não gera erro

# 4 - O que acontece se digitar zero a esquerda em python?

numero_zero_esquerda = 2
print(numero_zero_esquerda)

# Resposta: Zero a esquerda não são permitidos para inteiros decimais.
# SyntaxError: leading zeros in decimal integer literals are not permitted;
# use an 0o prefix for octal integers

# 5 - O que acontece se você tiver dois valores sem nenhum operador entre eles?

# numero_sem_operador = 2 2
# print(numero_sem_operador)

# Resposta: Erro de sintaxe
# SyntaxError: invalid syntax

# 6 - Quantos segundos há em 42 min e 42 segundos
min = 42
segundos_por_min = 60
segundos_informado = 42

total_segundos = (min * segundos_por_min) + segundos_informado
print(total_segundos)

# 7 - Quantas milhas a em 10 quilômetros?

uma_milha_KM = 1.61
qtd_km = 10

total_milha = qtd_km / uma_milha_KM
print(f'10 km equivale a {total_milha:.2f} milhas.')

# 8 - Se você correr 10km em 42 min e 42 seg, qual é o seu passo médio?
pace_segundos = total_segundos/qtd_km
print(f'Pace de {pace_segundos:.2f} segundos por KM.')

pace_minutos = (total_segundos/segundos_por_min)/qtd_km
print(f'Pace de {pace_minutos:.2f} minutos por KM.')

pace_segundos = total_segundos/total_milha
print(f'Pace de {pace_segundos:.2f} segundos por milhas.')

pace_minutos = (total_segundos/segundos_por_min)/total_milha
print(f'Pace de {pace_minutos:.2f} minutos por milhas.')

# Qual a velocidade média em milhas por horas?
total_minutos = total_segundos / 60
total_horas = total_minutos / 60
velocidade_media_milhas = total_milha / total_horas
print(f'Velocidade de {velocidade_media_milhas:.2f} milhas por horas.')
velocidade_media_km = qtd_km / total_horas
print(f'Velocidade de {velocidade_media_km:.2f} km por horas.')
