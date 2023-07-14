# Operadores Lógicos
# AND, OR, NOT, IN, NOT IN

# AND compara se duas comparações são verdadeiras
# comparacao1 and comparacao2

# OR compara se alguma da comparações são verdadeiras
# comparacao1 or comparacao2

# NOT comparador inverte o resultado de uma comparação
# inverte o resultado de uma comparação.

# IN verificar se um valor/dado existe
nome = 'alex sousa'
if 'a' in nome:
    print("Existe!")

# Not IN inverte e verificar se um valor/dado existe
nome = 'alex sousa'
if 'i' not in nome:
    print("Não Existe!")
else:
    print('Existe!')

usuario = input('Nome do usuário: ')
senha = int(input('Senha do usuário: '))

usuario_bd = 'alex'
senha_bd = 123456

if usuario == usuario_bd and senha == senha_bd:
    print(f'Usuário {nome} logado!')
else:
    print('Usuário ou Senha Inválido.')
