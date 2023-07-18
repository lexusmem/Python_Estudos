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

# funções build-in do Python para strings
print(type(texto))
print(dir(texto))
help(str)
