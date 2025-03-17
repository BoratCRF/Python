# 5) Escreva um programa que leia o valor de um produto e o percentual de desconto. O programa deve exibir o valor final com o desconto aplicado.

prod = float(input('Digite o valor do produto em R$: '))
desconto = int(input('Digite o percentual de desconto: '))
valorfinal = (desconto*prod)/100

print(f'Com desconto, o valor final fica em R${valorfinal}')