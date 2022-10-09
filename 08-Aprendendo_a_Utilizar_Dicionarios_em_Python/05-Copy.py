contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}
print(contatos["guilherme@gmail.com"])

print(copia["guilherme@gmail.com"])