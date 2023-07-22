# é possível acessar os indices das strings

texto = 'Estudando Python'
print('Número de indices dentro da string criada', len(texto))

# É possível acessar os indices com valores positivos
novo_texto = texto[0:7]
print(novo_texto)
novo_texto = texto[4:]
print(novo_texto)
novo_texto = texto[:8]
print(novo_texto)

# É possível acessar os indices passos
novo_texto = texto[0:12:2]
print(novo_texto)

# É possível acessar os indices com valores negativos
novo_texto = texto[-16:]
print(novo_texto)

novo_texto = texto[-13:-7]
print(novo_texto)

novo_texto = texto[-1:]
print(novo_texto)

# funções build-in upper (maiúscula) do Python para strings
print(texto.upper())

# funções build-in lower (minuscula) do Python para strings
print(texto.lower())

# Função builtin strip() remove espaços
# do começo e do fim da frase
frase = '    teste remoção de espaço.   '
print(frase)
print(frase.strip())
# Função builtin capitalize() primeira letra maiúscula.
print(frase.strip().capitalize())

# Sep utiliza uma string para separar.
# End inserir string no final do print
nome = "João"
idade = 30
print("Nome:",
      nome, "Idade:", idade, sep=" | ", end="\n==Acabou a Impressão==")

# Função builtin startswith('A')
# verifica primeira palavra
variavel = ['Alex Sousa', 'Pamela Rodrigues',
            'Gabriel Sousa', 'Bryan Sousa', 'Laura Sousa']
for nome in variavel:
    if nome.startswith('A'):
        print(nome, '- Começa com a letra "A".')
    else:
        print(nome, '- Não começa com a letra "A".')

# funções build-in do Python para strings
print(type(texto))
print(dir(texto))
help(str)
