class Aluno:
    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.notas = []

    def inserir_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)


aluno1 = Aluno(123, 'Lucas', 'B2')
aluno2 = Aluno(456, 'Luiz', 'B1')
aluno3 = Aluno(789, 'Luca', 'B2')

