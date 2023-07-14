"""
Iterando string com while
"""
minha_string = 'o rato roeu a roupa do rei de Roma.'

# Iterando com itens de uma string com laço while
cont = 0

while cont < len(minha_string):  # len contar numero de caracteres
    print(minha_string[cont])
    cont += 1

# Alterando string's com while
cont = 0
nova_string = ''

while cont < len(minha_string):
    if minha_string[cont] == 'r':
        nova_string = nova_string + minha_string[cont].upper()
    else:
        nova_string = nova_string + minha_string[cont]
        # Sinal de soma em string's concatena
        # ou poderia ser escrito desta forma:
        # nova_string += minha_string[cont]
    cont += 1
print(nova_string)

# Contagem de letras com while
cont = 0
contagem_atual = 0
letra = ''

print(minha_string.count('a'))

while cont < len(minha_string):
    qtd_das_letras = minha_string.count(minha_string[cont])

    # Função strip remove espaços
    if contagem_atual < qtd_das_letras and minha_string[cont].strip():
        letra = minha_string[cont]
        contagem_atual = qtd_das_letras

    cont += 1

print(letra.upper(), contagem_atual)
