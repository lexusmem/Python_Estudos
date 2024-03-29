import math
from unittest import result
# Funções
# Funções são sequencias nomeadas de instruções que executa
# uma operação de computação. Ao definir uma função, você
# especifica o nome e a sequencia de instruções. Depois,
# pode "chamar" a função pelo nome.

print(type(47))

# o nome da função é type e o dado no parênteses é o argumento da função.

# a função "recebe" um argumento e "retorno" um resultado
# chamado de valores de retorno.

# o python possui funções que convertem valores.

print(int('32'))
print(int(3.999))
print(float(32))
print(float('32.2514'))

# funções matemáticas.
# o python possui um módulo matemático, o módulo é um arquivo
# que possui uma coleção de funções relacionadas.

# antes de utilizar um módulo é preciso importa-lo:
# import math

print(math)
# print(help(math))

# o módulo possui funções e variáveis definidas no módulo.
# para acessa é preciso especificar o nome do módulo e o
# nome da função separados po ponto que é chamado de notação
# por ponto.

noise_power = 1
signal_power = 2

ratio = signal_power / noise_power
decibeis = 10 * math.log10(ratio)
radians = 0.7
height = math.sin(radians)

print(decibeis)
print(height)

degrees = 45
radians = degrees / 180.0 * math.pi
print(math.sin(radians))

comparacao = math.sqrt(2) / 2.0
print(comparacao)

# composição
# falamos de elementos de um programa - variáveis, expressões e instrução
# de forma isolada, mas não sobre como combiná-los

# por exemplo um argumentos de uma função pode ser qualquer tipo
# de expressão, inclusive operadores aritméticos:

x = math.sin(degrees / 360.0 * 2 * math.pi)
print(x)

# e até chamar funções:

x = math.exp(math.log(x+1))
print(x)

# o lado esquerdo de uma instrução de atribuição tem que ser um
# nome de variável. qq outra expressão do lado esquerdo da erro
# de sintaxe

hours = 13
minutes = hours * 60
print(minutes)

# hours * 60 = minute - ERRO

# como acrescentar novas funções
# É possível acrescentar novas funções em python.
# Uma definição de função especifica o nome de uma
# nova função e a sequência de instruções que são
# executadas quando a função é chamada


# exemplo:

# primeira linha chama-se cabeçalho (definição de função)
def print_lyrics():
    # E o corpo da função (com instruções)
    '''
    Função:\n
    Teste para impressão de texto na tela.
    \n
    Argumento:\n
    Não possuí.
    '''
    print("I'm a lumberjack, and I'm okay")
    print("I sleep all night and I work all day")

# def é uma palavra reservada que indica uma definição de função.
# O nome da função é "print_lyrics" que possui regra de nomeação
# as mesmas das variáveis
# os parênteses vazio indicam que esta função não possui argumentos.


print_lyrics()

# uma função pode ser atribuída a uma variável
# alex = print_lyrics()


# uma função pode ser utilizada dentro de outra função
def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()

# A definição de uma função cria um objeto de função
# que tem o tipo function:
print(print_lyrics)


# Podemos saber qual o seu tipo classe
print(type(print_lyrics))


# Uso de definições

# as funções acima possuem duas definições de funções:
# print_lyrics e repeat_lyrics
# as definições de função tem o objetivo de criar
# um objeto chamado função (function)
# e as instruções não são executadas até que a função seja chamada.
# Não é possível chamar a função antes de cria-lá

# Fluxo de execução.

# A execução sempre começa na primeira instrução do programa.
# As instruções são executadas uma após a outra de cima para baixo.

# Uma chamada de função é como se um desvio no fluxo da execução.
# Ao invés de ir à próxima instrução o fluxo salta para o corpo da função.

# Parâmetros e Argumentos

# Algumas funções exigem argumentos.
# Dentro da função, os argumentos são atribuídos a
# variáveis chamadas parâmetros.

def print_alex(alex):
    print(alex)
    print(alex)


# esta função atribui o argumento a um parâmetro chamado alex.
# Quando a função é chamada, ele exibe o valor do parâmetro 2x.

# esta função funciona com qualquer valor que possa ser exibido.
# Você pode até usar uma variável como argumento.


alex = 'ALEX'
print_alex(alex)
print_alex(42)
print_alex('teste nome alex')
print_alex(type(alex))
print_alex('teste nome alex' * 4)
print_alex(math.cos(math.pi))

# As Variáveis e os parâmetros são locais.

# uma variável dentro de uma função é local, ela só existe dentro da função.


def cat_twice(part1, part2):
    cat = part1 + part2
    print_alex(cat)


line1 = 'teste função '
line2 = 'teste função'
cat_twice(line1, line2)

# Quando a função é encerrada a variável cat é destruída.

# Ao tentar acessar a variável retornará erro:
# print(cat)
# NameError: name 'cat' is not defined

# Diagrama de pilhas

# diagrama de pilha é o desenho onde cada função é representada por um quadro
# (frame)e que cada frame possui as variáveis que pertence a cada função.

# Exemplo:

# __main__  ____________________________
#          | Line1----> 'teste função ' |
#          | Line2----> 'teste função'  |
#          | ___________________________|

# cat_twice _____________________________________
#          | part1----> 'teste função '          |
#          | part2----> 'teste função'           |
#          | cat---> 'teste função teste função' |
#          | ____________________________________|

# os frames são organizados em uma pilha para indicar
# qual função chamou a outra, no exemplo o cat_twice foi chamado por __main__

# Funções com resultado e funções nulas.

# quando vc chama uma função com resultado quase sempre você quer fazer algo
# com o resultado você pode atribuir a uma variável ou usá-la como parte de
# uma expressão.

x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

# quando chama afunção no modo interativo, o python exibe o resultado:
# >>>> math.sqrt(5)
# 2.2360679774997898

# mas em modo script o valor de retorno é perdido.
# math.sqrt(5)
# este script calcula a raiz quadrada e mais nada.

# as funções nulas podem exibir algo na tela ou ter algum outro efeito,
# porém não tem valor de retorno.

result = print_alex('Alex')

print(result)


# o valor 'None' é um valor especial que tem seu próprio tipo:

print(type(None))

# DEPURAÇÃO

# A depuração, também conhecida como "debugging", é o processo de encontrar
# e corrigir erros em um programa de computador. É um passo crucial no
# desenvolvimento de software para garantir que o programa funcione como
# esperado e atenda às suas necessidades.
