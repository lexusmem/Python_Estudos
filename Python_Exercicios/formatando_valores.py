'''
Formatando valores com modificadores

:s - Texto (string)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (NÚMERO)f - Quantidade de casas decimais (float)
: (CARACTERE) (> ou <) (QUANTIDADE) (TIPO - s, d ou f)
'''

# > - Esquerda
# < - Direita
# ^ - Centro
num_1 = 10
num_2 = 3
resultado = num_1 / num_2
print(resultado)
print(f'O resultado da divisão é {resultado:.2f}.')

num_3 = 1
print(f'{num_3:.2f}')
print(type(num_3))

num_3 = 1
print(f'{num_3:0>10}')

num_4 = 1150
print(f'{num_4:0<10}')
print(f'{num_4:0<10.2f}')

num_5 = 1150
print(f'{num_4:0^10}')

nome = 'Alex Sousa'
print(f'{nome:#^50}')

nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

nome_formatado = '{n:0<50}'.format(n=nome)
print(nome_formatado)

nome = 'Alex'
sobrenome = 'Sousa'
nome_formatado = '{1}'.format(nome, sobrenome)
print(nome_formatado)
nome_formatado = '{1:#^50}'.format(nome, sobrenome)
print(nome_formatado)
print(nome_formatado.upper())
print(nome_formatado.lower())
