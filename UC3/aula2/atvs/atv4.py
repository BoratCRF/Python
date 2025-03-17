# 4) Crie um programa que leia três notas de um aluno e calcule a média aritmética.

nota1 = float(input('Digite a nota 1 do aluno: '))
nota2 = float(input('Digite a nota 2 do aluno: '))
nota3 = float(input('Digite a nota 3 do aluno: '))

med = (nota1+nota2+nota3)/3

print(f'A nota do aluno é: {med:.1f}')