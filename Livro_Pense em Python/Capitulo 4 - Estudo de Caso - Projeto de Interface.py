import turtle

# Este estudo de caso demonstra o processo de criação de funções que operam
# simultaneamente.

# Apresenta o módulo turtle que permite criar imagens usando [turtle graphics]

# Módulo turtle
# import turtle


# módulo turtle (t minusculo) função Turtle(T maiúsculo).
# Que cria um objeto Turtle, que está atribuído a variável Bob
bob = turtle.Turtle()
bob2 = turtle.Turtle()
print(bob)

# uma vez criado o Turtle pode chamar um método para move-lo para frente.
# .fd(valor) - mover para frente
# .bk(valor) - mover para para trás
# O método fd e bk é uma distância em pixeis, então depende do tamanho
# real da tela.
bob.fd(100)

# .lt(valor) - vira a esquerda
# .rt(valor) - vira a direita
# O método lt e rt o argumento é um angulo em graus.
bob.lt(90)
bob.fd(100)

# Cada turtle segura uma caneta podendo a caneta esta abaixada (deixa rastro) .pd()
# E para cima (não deixa rastro) .pu()

bob2.pu()
bob2.bk(100)
bob2.lt(90)
bob2.pd()
bob2.fd(100)

# 4.2 Repetição Simples
# Conforme escrita acima trata-se de uma repetição simples.
# podemos faser algo mais conciso com uma instrução for.

for i in range(4):
    print('Hello!')

# aqui está uma instrução for que desenha um quadrado

bob3 = turtle.Turtle()

for i in range(4):
    bob3.fd(50)
    bob3.lt(90)

# Uma instrução for também é chamada de loop.

# mainloop diz que a janela deve esperar o usuário fechar a janela.
# Deve fica no fim do código.

turtle.mainloop()
