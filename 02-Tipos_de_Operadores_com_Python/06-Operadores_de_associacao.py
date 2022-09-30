# São operadores utilizados para verificar se um objeto está presenta em uma sequência
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

print("Python" in curso)

#Ele é case sentive (no caso abaixo, apesar da palavra python está em curso, ela está com o P maiúsculo)
print("python" in curso)

print("laranja" in frutas)

print("maça" in frutas)

print(300 in saques)