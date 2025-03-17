# 3) Crie um programa que leia um valor em reais (R$) e mostre o valor convertido em dólares (US$), considerando uma taxa de câmbio fornecida pelo usuário.

reais = float(input('Digite o valor em R$: '))
taxa = float(input('Digite a taxa de câmbio: '))

dolar = reais/taxa

print(f'O valor em dóla, dos R${reais} convertidos em uma taxa de R${taxa}, é de US${dolar:.1f}')