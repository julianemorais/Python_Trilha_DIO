#São utilizados para comparar se dois objetos estão testados ocupam a mesma posição na memória.
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)