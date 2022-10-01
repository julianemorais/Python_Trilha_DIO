linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens)

linguagens.sort()

print(linguagens)

linguagens.sort(reverse=True)

print(linguagens)

# Ordernar pelo tamanho da palavra
linguagens.sort(key=lambda x: len(x))

print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True)

print(linguagens)

