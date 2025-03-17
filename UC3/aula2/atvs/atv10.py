# 10) Considere que o preço da tarifa de energia é R$ 0,50 por kWh.
# Pergunte ao usuário o consumo de energia em kWh e calcule o valor total a ser pago pela conta. Se o consumo for maior que 200 kWh, aplique um desconto de 10%.

consumo = float(input("Digite a quantidade de consumo em kWh: "))
tarifa = 0.50
valor_total = tarifa*consumo
desconto = 10
if consumo < 200:
    print(f'O valor total a ser pago, pelo consumo de {consumo}kWh, será de: R${valor_total:.2f}')
else:
    valor_total_descontado = (desconto*valor_total)/100
    print(f'O valor total a ser pago, pelo consumo de {consumo}kWh, será de: R${valor_total - valor_total_descontado:.2f}')
