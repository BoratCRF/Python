# 7) Escreva um programa que receba três números inteiros e determine qual deles é o maior.

num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))
num3 = int(input("Digite o número 3: "))

if num1 > num2 and num1 > num3:
    print(f'O {num1} é maior que os números {num2} e {num3}')
elif num2 > num1 and num2 > num3:
    print(f'O {num2} é maior que os números {num1} e {num3}')
else:
    print(f'O número {num3} é o maior entre eles')
