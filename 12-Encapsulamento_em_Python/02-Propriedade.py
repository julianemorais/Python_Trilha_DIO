class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa("Juliane", 1972)
print(f"Nome: {pessoa.nome} \t Idade: {pessoa.idade}")