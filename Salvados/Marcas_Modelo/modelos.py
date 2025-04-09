import ast

with open(r'C:\Users\lexus\Documents\Estudos\Python_Estudos\Salvados\Marcas_Modelo\veiculos.sql', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.readlines()
print(type(conteudo))
print(len(conteudo))

modelos = []

for linha in conteudo:
    linha = linha.strip()
    if linha.startswith("(") and linha.endswith("),"):
        cont = ast.literal_eval(linha)
        for linha_1 in cont:
            modelos.append(list(linha_1))


resultado = [sublista for sublista in modelos if len(sublista) < 3]


lista_final = []
for valor in resultado:
    if valor[1] not in lista_final:
        lista_final.append(valor[1])

print(lista_final)
