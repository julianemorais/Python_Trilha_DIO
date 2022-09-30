nome = "Juliane"

#Tudo Maiúculo
print(nome.upper())

#Tudo Minúsculo
print(nome.lower())

#Primeira letra maiúscula
print(nome.title())

#Eliminando espaçoes em branco

texto = "   Curso de Python   "

print(texto + ".")
print(texto.strip() + ".")

#Eliminando espaco em branco a esquerda
print(texto.lstrip() + ".")

#Eliminando espaço em branco a direita
print(texto.rstrip() + ".")

#centralização
print(nome.center(15, "#"))

#Junção
print(".".join(nome))