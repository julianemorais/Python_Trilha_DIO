class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objetos):
    for objeto in objetos:
        print(objeto)
    
aluno_1 = Estudante("Juliane", 1)
aluno_2 = Estudante("Ricardo", 2)

mostrar_valores(aluno_1, aluno_2)

