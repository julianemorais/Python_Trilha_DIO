contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.setdefault("nome", "Giovanna")
print(contatos)

contatos.setdefault("idade", 28)
print(contatos)