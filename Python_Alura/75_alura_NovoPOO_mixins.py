class Funcionario:
    def __init__(self, nome):
        self.nome = nome.title()

    def registra_hora(self, horas):
        print(f"{horas} Hora Registrada...")

    def tarefa(self):
        print('Tarefas executadas!')


class Caelum (Funcionario):
    def mostrar_tarefas(self):
        print(f'{self.nome} fez muitas coisas. Caelumer!')

    def buscar_curso_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}'
              if mes else 'Mostrando curso deste mês.')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print(f'{self.nome} fez muitas coisas. Alurete!')

    def busca_perguntas_sem_respostas(self):
        print('Mostrando perguntas não respondidas.')


# Classe MIXIN
class Hipster:
    def __str__(self):
        return f'{self.nome} Hipster.'


# Classe com herança de uma única classe
class Junior(Caelum):
    pass


# Classe com mais de herança de uma classe
# Herança Múltipla
class Pleno(Alura, Caelum):
    pass


class Senior(Alura, Caelum, Hipster):
    pass


alex = Junior("alex")
# Método da classe funcionários
alex.registra_hora("10:20")
# Método da classe Caelum
alex.mostrar_tarefas()
# Método da classe Alura
# Gera erro pois a classe junior não possui
# herança com os métodos da classe Alura
# alex.busca_perguntas_sem_respostas()

pamela = Pleno("pamela")
pamela.mostrar_tarefas()


laura = Senior("laura")
print(laura)

# MRO
# Define a ordem para busca de métodos nas classes
# Exemplo método "mostrar_tarefas"
# Consta nas 3 classes Funcionários/Caelum/Alura

# Retorno
# pleno > alura > funcionários > caelum > funcionários
# No código acima o caelum é um método good head sobre funcionário
# por esse motivo a sequência passa a ser:
# pleno > alura > caelum > funcionários
