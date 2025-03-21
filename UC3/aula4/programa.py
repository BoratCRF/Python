#capturar erro por divisão e erro por dado inválido
# a = 2
# b = 0
# try:
#     c = a/b
#     print(c)
# except:
#     print("Erro: Divisão por zero não é permitida")
#                  -------------------------------------
# try:
#     x = int(input("Digite um número: "))
#     resultado = 10/x
#     print(f'{round(resultado,2)}')
# except ZeroDivisionError:
#     print("Erro: Divisão por zero não é permitida")
# except ValueError:
#     print("Erro: Só é permitida a entrada de números inteiros")    

# **************************************************************************************************

# usando o finally para limpeza

# try:
#     arquivo = open('dados.txt')
#     conteudo = arquivo.read()
#     print(conteudo)
# except FileNotFoundError:
#     print("Erro: Arquivo não encontrado")
# finally:
#     if 'arquivo' in locals():
#         arquivo.close()
#         print("Arquivo fechado com sucesso")

# *****************************************************************************************************


# Definir a própria exceção. Criar manualmente

try:
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        raise ValueError("A idade não pode ser negativa.")
    print(idade)
except ValueError as ve:
    print(f'Erro: {ve}')
except Exception as e:
    print(f"Erro: {e}")