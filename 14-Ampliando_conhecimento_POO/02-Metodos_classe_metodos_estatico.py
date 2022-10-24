class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_nascimento(cls, dia, mes, ano, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    
p = Pessoa.criar_data_nascimento(2, 8, 1972, "Julaine")
print(p.nome, p.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(8))