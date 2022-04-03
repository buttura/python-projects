from random import choice
n = list()
for i in range(0, 4):
    n.append(str(input(f"Digite o nome do {i+1}o aluno: ")))
print(f"Aluno escolhido: {choice(n)}")
