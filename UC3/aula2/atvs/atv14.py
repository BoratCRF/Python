# 14) Solicita um valor e um percentual de desconto, e calcula o valor final.

valor = float(input('Digite o valor em R$: '))
desconto = int(input('Digite o percentual de desconto: '))
valorfinal = (desconto*valor)/100

print(f'Com desconto de {desconto}%, o valor final fica em R${valorfinal}')