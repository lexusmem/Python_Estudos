idade1 = 39
idade2 = 39
idade3 = 39
# coleções - diversos valores  - list
idades = [12, 40, 34, 36, idade1, idade2]
print(idades)


# problemas das listas serem mutáveis
# Função que altera a lista e está ai o problema
# passar como parâmetro um objeto mutável
# no retorno da função pode ter ocorrido a total
# desconfiguração da sua lista
def faz_processamento_visualizacao(lista):
    print(len(lista))
    lista.append(22)


faz_processamento_visualizacao(idades)
print(idades)
faz_processamento_visualizacao(idades)
print(idades)


# Outra consequência
# criar função com valor padrão
# O objetos esta referenciado e não deixa de existir
# e toda chamada desta função incrementa e executa
# o que consta na função
def faz_processamento_padrao(lista=[]):
    print(len(lista))
    print(lista)
    lista.append(22)


print(faz_processamento_padrao())
print(faz_processamento_padrao())
print(faz_processamento_padrao())


# para corrigir
def faz_processamento_padrao1(lista=None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(22)


print(faz_processamento_padrao1())
print(faz_processamento_padrao1())
print(faz_processamento_padrao1())
