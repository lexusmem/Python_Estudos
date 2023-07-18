"""
For in
Iterando strings com for
Função range(start=0, stop, step=1)
"""
texto = 'python'

for letra in texto:
    print(letra)
print('=====')

for indice, letra in enumerate(texto):
    print(indice, letra)
print('=====')

# For com Função range(start=0, stop, step=1)
for numero in range(10):
    print(numero)
print('=====')

# Argumentos - Range (start=0, stop, step=1)
for numero in range(5, 10, 2):
    print(numero)
print('=====')

# Argumentos - Range (start=0, stop, step=1)
for numero in range(5, 10, 2):
    print(numero)
print('=====')

# Decrementação - Range (start=0, stop, step=1)
for numero in range(20, 10, -1):
    print(numero)
print('=====')

# Múltiplos - Range (start=0, stop, step=1)
for numero in range(0, 100, 8):
    print(f'{numero} múltiplo de 8.')

print()

for numero in range(100):
    if numero % 8 == 0:
        print(f'{numero} múltiplo de 8.')
print('=====')

nova_string = ''
for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)
print('=======')

nova_string_1 = ''
for letra in texto:
    if letra == 't':
        continue
        nova_string_1 = nova_string_1 + letra.upper()
    elif letra == 'h':
        nova_string_1 += letra.upper()
        break
    else:
        nova_string_1 += letra
print(nova_string_1)
print('=======')
