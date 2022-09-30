from platform import python_branch


nome = "Juliane"
idade = 50
profissao = "Analista de Suporte" 
linguagem = "Python"

pessoa = {"nome": "Juliane", "idade": 50, "profissao": "Analista de Suporte", "linguagem": "Python"}

#Old Style %
#%s variável string, %d variável inteiro, variáveis tem  seguir a ordem.
print("Olá, meu nome é %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculada no cruso de %s." %(nome, idade, profissao, linguagem))

#Metódo Format
print("Olá, meu nome é {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculada no cruso de {}." .format(nome, idade, profissao, linguagem))

print("Olá, meu nome é {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no cruso de {linguagem}." .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("Olá, meu nome é {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no cruso de {linguagem}." .format(**pessoa))

# f-string (O melhor deles)
print(f"Olá, meu nome é {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no cruso de {linguagem}.")

#Formatar strings com f-string
PI = 3.14159

print(f"Valor de PI: {PI:.2f}")  # O .2 quer dizer duas casas após a vírgula