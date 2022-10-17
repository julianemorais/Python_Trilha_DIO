class Animal():
    def __init__(self, nr_patas):
        self.nr_patas = nr_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw): 
        self.cor_bico = cor_bico      
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nr_patas):  
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nr_patas=nr_patas)

gato = Gato(nr_patas=4, cor_pelo="Branco")
print(gato)

ornitorrinco = Ornitorrinco(nr_patas=2, cor_pelo="Cinza", cor_bico="Preto")
print(ornitorrinco)