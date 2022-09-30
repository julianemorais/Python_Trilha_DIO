#if
MAIOR_IDADE = 18        #Constante
IDADE_ESPECIAL = 17     #Constante

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, você pode tirar CNH")
    
if idade <= MAIOR_IDADE:
    print("Menor idade, você ainda não pode tirar CNH.")
    
#else
if idade >= MAIOR_IDADE:
    print("Maior de idade, você pode tirar CNH")
else:
    print("Menor idade, você ainda não pode tirar CNH.")

#elif
if idade >= MAIOR_IDADE:
    print("Maior de idade, você pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Você pode fazer as aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Menor idade, você ainda não pode tirar CNH.")