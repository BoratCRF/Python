# LENDO UM ARQUIVO

# file = open('dados.txt', 'r')
# print(file.read())
# file.close

# Sobrescrevendo o conteúdo de um arquivo e lendo em seguida

# with open('dados.txt', 'w') as file:
#     file.write('Ele é, ele é')
# file = open('dados.txt', 'r')
# print(file.read())
# file.close

# Gravando o conteúdo de um arquivo, dentro de uma variável

# with open('dados.txt', 'r') as file:
#     conteudo = file.read()
#     print(conteudo)

#  Criando um arquivo nomes.txt, preenchendo e imprimindo ele

with open('nomes.txt', 'w') as file:
    file.write('Ana\nCarlos\nBruno')

with open('nomes.txt', 'r') as file:
    print(file.read())