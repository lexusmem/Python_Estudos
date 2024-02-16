import math
import signal
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

# o módulo possui funções e variáveis definidas no módulo.
# para acessa pe preciso especificar o nome do módulo e o
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

# parei no item 3.4
