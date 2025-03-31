class Carro:
    def __init__(self, modelo, placa, ano):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

def ligar(self):
    print(f'Ligando o carro {self.modelo}: Vruuuuum')

def parar(self):
    print(f'Freiando o carro {self.modelo}: iiiiiir.')

def mostrar(self):
    print(f'Hoje apresentamos o carro {self.modelo} de placa {self.placa} fabricado no ano de {self.ano}.')

carro1 = Carro("Mustang", "BRA2E22", 2022)
mostrar(carro1)
ligar(carro1)
parar(carro1)