class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Buzinando")
    
    def parar(self):
        print("Freiando a bicicleta...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Pedalando a bicicleta")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
caloi = Bicicleta("Vermelha", "Mountain Bike", 2022, 1000)
caloi.buzinar()
caloi.correr()
caloi.parar()

print(caloi)
    