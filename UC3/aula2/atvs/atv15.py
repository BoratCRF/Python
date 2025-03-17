# 15) Solicita três notas de um aluno, calcular a média e informar se ele está aprovado ou não, considerando a média de aprovação maior ou igual a 6.

nota1 = float(input('Digite a nota 1 do aluno: '))
nota2 = float(input('Digite a nota 2 do aluno: '))
nota3 = float(input('Digite a nota 3 do aluno: '))

med = (nota1+nota2+nota3)/3
if med >= 6:
    print(f'A nota do aluno é {med:.1f}: APROVADO')
else:
        print(f'A nota do aluno é {med:.1f}: REPROVADO')
