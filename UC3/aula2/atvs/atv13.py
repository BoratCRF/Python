# 13) ler altura e peso, e informar o imc e qual a situação do indivíduo

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/(altura*2)
if imc < 18.5:
    print(f'Seu IMC é: " {imc} você está abaixo do peso')
elif imc >= 18.5 and imc <= 24.99:
    print(f'Seu IMC é: {imc:.2f} você está com o Peso normal')
elif (imc >= 25 and imc <= 29.99):
    print(f'Seu IMC é: {imc:.2f} você está com Sobrepeso')
elif (imc >= 30 and imc <= 34.99):
    print(f'Seu IMC é: {imc:.2f} você está com Obesidade I')
elif (imc >= 35 and imc <= 39.99):
    print(f'Seu IMC é: {imc:.2f} você está com Obesidade II')
elif (imc >= 40):
    print(f'Seu IMC é: {imc:.2f} você está com Obesidade III')
else:
    print("Peso inválido")
  