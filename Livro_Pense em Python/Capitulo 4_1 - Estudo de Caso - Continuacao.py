import turtle

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


polygon(bob, 8, 55)

# 4.6 Projeto de interface - parei aqui
