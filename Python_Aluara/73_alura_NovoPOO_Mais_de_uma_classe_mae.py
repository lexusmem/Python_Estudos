class Funcionario ():
    def registra_hora(self, horas):
        print(f"{horas} Hora Registrada...")

    def tarefa(self):
        print('Tarefas executadas!')


class Caelum (Funcionario):
    def mostrar_tarefas(self):
        print('Fez muitas coisas. Caelumer!')

    def buscar_curso_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}'
              if mes else 'Mostrando curso deste mês.')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muitas coisas. Alurete!')

    def busca_perguntas_sem_respostas(self):
        print('Mostrando perguntas não respondidas.')

# Classe com herança de uma única classe


class Junior(Caelum):
    pass

# Classe com mais de herança de uma classe


class Pleno(Alura, Caelum):
    pass


alex = Junior()
# Método da classe funcionários
alex.registra_hora("10:20")
# Método da classe Caelum
alex.mostrar_tarefas()
# Método da classe Alura
# Gera erro pois a classe junior não possui
# herança com os métodos da classe Alura
# alex.busca_perguntas_sem_respostas()

pamela = Pleno()
pamela.mostrar_tarefas()
