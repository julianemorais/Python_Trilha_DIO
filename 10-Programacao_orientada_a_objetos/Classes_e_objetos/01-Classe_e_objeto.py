# Classe
class Cachorro:
    def __init__(self, nome, cor, acordado=True): # self é a instância do objeto que foi passado
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
            
    def latir(self):
        print("AUAU")
        
    def dormir(self):
        self.acordado = False
        print("Zzzzz")
 
# Objeto       
cao_1 = Cachorro("Chappie", "Amarelo", False)
cao_2 = Cachorro("Aladim", "Branco e Preto")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)