import math
import turtle


def square(t, length):
    """desenho quadrado

    t: Turtle
    length: tamanho dos lados
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()


def polygon(t, n, length):
    """desenho polígono

    t: Turtle
    n: numero de lados
    length: tamanho dos lados
    """
    for i in range(n):
        angulo = (360 / n)
        t.fd(length)
        t.lt(angulo)
    turtle.mainloop()


# Escreva uma função chamada circle que use o turtle t e um raio r como
# parâmetros e desenhe um círculo aproximado ao chamar polygon com um
# comprimento e número de lados adequados.

# Dica: descubra a circunferência do círculo e certifique-se de que length * n = circumference

def circle(t, r):
    '''desenho circulo
    t: Turtle
    r: raio do circulo
    '''
    circunferencia = (2 * math.pi * r)
    n = int(circunferencia / 3)
    length = (circunferencia / n)
    polygon(t, n, length)

# faça uma versão mais geral do circle chamada arc, que receba um parâmetro
# adicional de angle, para determinar qual fração do círculo deve ser desenhada
# angle está em unidades de graus, então quando angle=360, o arc deve desenhar
# um círculo completo.


def arc(t, r, angle):
    '''desenho circulo
    t: Turtle
    r: raio do circulo
    angle: ??????
    Exercício não concluído.
    '''
    circunferencia = 2 * math.pi * r
    n = int(circunferencia / 3)
    length = circunferencia / n
    polygon(t, n, length)


bob = turtle.Turtle()

# square(bob, 250)
# polygon(bob, 7, 100)
circle(bob, 50)
