# Função entrada de dados INPUT
# Sempre um input gera uma string
nome = input('Qual o seu nome: ')
idade = int(input('Qual o seu nome: '))
print(f'Seu nome é {nome} e o tipo da variável é {type(nome)}.')

ano_nascimento = 2023 - idade
print(f'Ano de nascimento {ano_nascimento}.')

print(f'{nome} tem {idade}.\n'
      f'{nome} nasceu em {ano_nascimento}.')
