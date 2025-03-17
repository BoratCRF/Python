# 1) Faça um programa que leia dois números e mostre a soma, a subtração, a multiplicação e a divisão entre eles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1+num2
sub = num1-num2
multi = num1*num2
div = num1/num2

print(f'A soma de {num1} e {num2} é: {soma}')
print(f'A subtração de {num1} e {num2} é: {sub}')
print(f'A multiplicação de {num1} e {num2} é: {multi}')
print(f'A divisão de {num1} e {num2} é: {div}')