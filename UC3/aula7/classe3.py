# class Aluno:
#     def __init__(self, nome, curso, tempoSemDormir):
#         self.nome = nome
#         self.curso = curso
#         self.tempoSemDormir = tempoSemDormir
#     def estudar(self, qtdHorasEst):
#         self.tempoSemDormir += qtdHorasEst
#         print(f'O Aluno {self.nome} estudou durante {qtdHorasEst}')
#     def dormir(self, qtdHorasDorm):
#         self.tempoSemDormir-= qtdHorasDorm
#         print(f'O Aluno {self.nome} dormiu {qtdHorasDorm} dentro de 24hrs')

#     def tempo(self):
#         print(f'O aluno {self.nome} ficou {self.tempoSemDormir}hrs sem dormir')

# aluno1 = Aluno("Vinicius", "Senac", 0)

# aluno1.estudar(8)
# aluno1.dormir(8)
# aluno1.tempo()

class Aluno:
    def __init__(self, nome, curso, tempoSemDormir=0):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def estudar(self, qtd_horas):
        self.tempoSemDormir += qtd_horas

    def dormir(self, qtd_horas):
        self.tempoSemDormir -= qtd_horas
        if self.tempoSemDormir < 0:
            self.tempoSemDormir = 0

# Teste da classe
aluno1 = Aluno("João", "Engenharia")
aluno1.estudar(8)
aluno1.dormir(6)
aluno1.estudar(4)
print(f"O aluno {aluno1.nome} está sem dormir há {aluno1.tempoSemDormir} horas.")