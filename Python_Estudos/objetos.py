idade = 27
idade_texto = '27'

# type () retorna o tipo de dado que contem o objeto.
# dir () retorna lista de métodos do objeto.
# help () retorna ajuda sobre o que o métodos executa.

tipo_idade = type(idade)
tipo_idade_texto = type(idade_texto)

metodos_idade = dir(idade)
metodos_idade_texto = dir(idade_texto)

print(
    f'O objeto idade possuí o dados {idade} que é do tipo {tipo_idade}.\n'
    f'A lista de métodos disponíveis para esta dado é:\n{metodos_idade}\n')

print(f'O objeto idade_texto possuí o dados {idade_texto} '
      f'é do tipo {tipo_idade_texto}. A lista de métodos disponíveis para esta'
      f' dado é: \n{metodos_idade_texto}\n')

nome = 'alex'
print(f'\nNovo objeto criado "nome" que possuí o dado: {nome}. '
      f'Do tipo {type(nome)}.')

print(
    f'Alterado o objeto "nome" com o método "capitalize" passou a ser: '
    f'{nome.capitalize()}.')

help(nome.capitalize)
