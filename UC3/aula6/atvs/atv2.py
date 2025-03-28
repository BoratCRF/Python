# Uma empresa fornece um arquivo de texto com nomes e idades dos
# funcionários. A tarefa é:


# Exibir
# os dados no console.
# Calcular a média das
# idades.
# Permitir
# ao usuário adicionar ou remover funcionários.


with open('funcionarios.txt', 'w') as file:
    file.write('Anna, 25\n')
    file.write('Maria, 30\n')
    file.write('Alice, 28\n')
    
with open('funcionarios.txt', 'r') as file:
    print(file.read())

with open('funcionarios.txt', 'r') as file:
    funcionarios = file.readlines()
    idades = [float(funcionario.split(",")[1]) for funcionario in funcionarios]
    media = sum(idades) / len(idades)
    print(f'Idade média dos Funcionários: {media:.2f}')
          
print('***********************************')

          
while True:
    resp = input("Gostaria de adicionar mais algum funcionário? (S/N): ").strip().upper()
    
    if resp == 'S':
        nvfunc = input("Digite o novo funcionário e sua idade: ")
        with open('funcionarios.txt', 'a') as file:
            file.write(nvfunc + '\n')
    else:
        print("Esses são todos os nossos funcionários:\n")
        with open('funcionarios.txt', 'r') as file:
            print(file.read())
        break

