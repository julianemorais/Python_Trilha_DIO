class Cachorro:
    def __init__(self, nome, cor, acordado=True): # self é a instância do objeto que foi passado
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):
        print("Removendo a instância da classe.")
        
            
    def latir(self):
        print("AUAU")
        
cao = Cachorro("Chappie", "Amarelo", False)   
cao.latir() 