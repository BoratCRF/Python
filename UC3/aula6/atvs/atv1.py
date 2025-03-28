with open('produtos.txt', 'w') as file:
    file.write('Arroz, 20\nFeijão, 15\nAçúcar, 10')

with open('produtos.txt', 'r') as file:
    print(file.read())

print('***********************************')

with open('produtos.txt', 'a') as file:
    file.write('\nFarinha, 5')

with open('produtos.txt', 'r') as file:
    print(file.read())

print('***********************************')

media = int(20+15+10+5)/4


with open('produtos.txt', 'w') as file:
    file.write('Arroz, 20\nFeijão, 15\nAçúcar, 10\nFarinha, 5')
    file.write(f'\n Média dos produtos é {media}')

with open('produtos.txt', 'r') as file:
    print(file.read())
