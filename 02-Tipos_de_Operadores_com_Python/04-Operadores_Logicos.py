saldo = 1000
saque = 200
limite = 100
conta_especial = True
contato_emergencia = [] #Lista vazia

print(saldo >= saque)
print(saque <= limite)

#Operador E / AND
print(saldo >= saque and saque <= limite)

#Operador OU / OR
print(saldo >= saque or saque <= limite)

#Operador de negação
print(not 1000 > 1500)

print(not contato_emergencia)

print(not "saque 1500")

print(not "")

#Parenteses
print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))