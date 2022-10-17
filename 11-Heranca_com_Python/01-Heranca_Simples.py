from traceback import print_tb


class Veiculo:
    def __init__(self, cor, placa, n_rodas):
        self.cor = cor
        self.placa = placa
        self.n_rodas = n_rodas

    def ligar_motor(self):
        print("Ligando motor")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, n_rodas, carregado):
        super().__init__(cor, placa, n_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "acd-4567", 4)
caminhao = Caminhao("Vermelho", "dfr-6789", 8, False)

print(moto)
print(carro)
print(caminhao)