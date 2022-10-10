def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"\n{data_extenso}\n\n{texto}\n\n{meta_dados}"
    
    print(mensagem)
    
exibir_poema("Segunda-feira, 10 de Outubro de 2022",
             "Zen on Python",
             "Beautiful is better than ugly.",
             "Explicit is better than implicit.",
             "Simple is better than complex.",
             "Flat is better than nested.",
             "Sparse is better than dense.",
             "Readability counts."  
             "Special cases aren't special enough to break the ruler.",
             autor="Tim Peters",    
             ano=1999,
)