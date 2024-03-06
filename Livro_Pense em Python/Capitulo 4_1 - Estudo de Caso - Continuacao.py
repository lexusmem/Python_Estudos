import turtle
import math

# 4.4 Encapsulamento
# A ideia é que o atributo t da função square pode ser qualquer turtle
# e não apenas bob podendo ser criado um segundo turtle e passá-lo como
# argumento da função square


def square(t):
    '''
    t: é o turtle
    '''
    for i in range(4):
        t.fd(100)
        t.lt(90)
    turtle.mainloop()


bob = turtle.Turtle()
# square(bob)

# alice = turtle.Turtle()
# square(alice)

# Incluir uma parte do código em uma função chama-se encapsulamento.
# Um dos benefícios do encapsulamento é que ele atribui um nome ao código
# o que serve como uma especie de documentação.
# Outra vantagem é que se você reutilizar o código, é mais conciso chamar uma
# função duas vezes que copiar e colar o corpo.

# 4.5 Generalização
# Na função abaixo acrescentamos um parâmetro chamado length, que define
# o tamanho do quadrado. Acrescentar um parâmetro a uma função chama-se
# generalização porque a função fica mais geral: agora é possível atribuir
# o tamanho do quadrado.


def square_generalizacao(t, length):
    '''
    t: é o turtle
    length: é o tamanho que cada lado do quadrado terá
    '''
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()


# square_generalizacao(bob, 100)

# O proximo passo também é uma generalização, a função desenhara polígonos
# retângulos com qualquer número de lados, na função terá acréscimo de mais
# um parâmetro.


def polygon(t, n, length):
    '''
    t: é o turtle
    n: número de lados do polígono
    length: é o tamanho que cada n terá
    '''
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    turtle.mainloop


# 4.6 Projeto de interface
# O próximo passo é escrever uma função circle.
# Ela recebe um raio r como parâmetro com um polígono de 50 lados.


def circle(t, r):
    """
    t: é o turtle

    Diâmetro da circunferência é um segmento de reta que passa pelo centro
    da figura, dividindo-a em duas metades.

    r: raio do círculo

    raio de um círculo é a distância do centro do círculo a qualquer
    ponto da circunferência.

    n: número de lados do polígono
    length: é o tamanho que cada n terá
    """
    circunferencia = 2 * math.pi * r
    n = 50
    length = circunferencia / n
    polygon(t, n, length)


# circle(bob, 100)

# Uma limitação da solução acima é que n é uma constante 50.
# Para círculos muito grande, os segmentos de reta são longos, e
# para círculo pequenos perdemos tempo desenhando segmentos pequenos.
# Uma solução seria generalizar n com parâmetro, dado ao usuário mais controle.

# A interface de uma função é um resumo de como ela é usada:
# Quais os parâmetros? O que a função faz? E qual o valor de retorno?
# Uma interface limpa permite que a chame para fazer o que quiser sem ter
# que lidar com os detalhes.

# em vez de poluir a interface é melhor escolher um valor adequado para n,
# dependendo da circunferência:


def circle_2(t, r):
    '''
    t: é o turtle

    r: raio do círculo
    '''
    circunferencia = 2 * math.pi * r
    n = (int(circunferencia / 3) + 1)
    length = circunferencia / n
    polygon(t, n, length)


# circle_2(bob, 500)

# 4.7 - Refatoração
# Criando um arco (arc)


def arc(t, r, angle):
    '''
    t: turtle

    r: raio

    angle: angulo do arco
    '''
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
    turtle.mainloop()


# arc(bob, 100, 90)

# a segunda metade da função acima poderia ser uma nova função.
# criar a função polyline generalida com o novo argumento angle.


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# agora podemos reescrever polygon e arc para usar polyline:


def polygon_2(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc_2(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


def circle_3(t, r):
    arc(t, r, 360)

# Este processo de recompor um programa para melhorar é chamado de refatoração


# circle_3(bob, 50)
arc_2(bob, 100, 180)

# 4.8 - Um plano de desenvolvimento

# Um plano de desenvolvimento é um processo que usamos para escrever programas.
# O processo utilizado neste estudo foi 'encapsulamento e generalização'

# 1 - Comece escrevendo um pequeno programa sem definições de funções
# 2 - Com o programa funcionando identifique uma parte coerente dele,
# encapsule essa parte em função e dê um nome a ela.
# 3 - generalize as funções acrescentando os parâmetros adequados.
# 4 - repita os passos 1 - 3 até que tenha um conjunto de funções operantes.
# 5 - Procura oportunidade de melhorar o programa.
# Se tiver um código semelhante em vários lugares pode ser uma boa ideia fatorá-lo
# em uma função geral adequada.

# 4.9 docstring - parei aqui
