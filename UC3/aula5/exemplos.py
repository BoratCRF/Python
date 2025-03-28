# compressão de listas
# exemplo 1

# =====================
x = [1,2,3,4]
y = []
j = []

for i in x:
     y.append(i**2)
print(y)
# ============================
w = [i**2 for i in x]
print(w)
# ============================
for i in x:
    if i % 2 == 0:
        j.append(i)

# =====================
j = [i for i in x if i % 2 == 0]
print()
# enumeração de lista
# exemplo 2 (enumeração de lista)
lista = ['abacate', 'abacaxi','melão','ameixa','maçã']
for i in range(len(lista)):
    print(i, lista[i])

# A função enumerate() em Python é usada para iterar sobre uma sequência
# como uma lista, tupla ou string e obter tanto o índice (posição) quanto o
# valor de cada item da sequência ao mesmo tempo

for i, fruta in enumerate(lista):
    print(i, fruta)

# Buscando caracteres
texto = "Python"

for indicie, caractere in enumerate(texto):
    print(indicie, caractere)