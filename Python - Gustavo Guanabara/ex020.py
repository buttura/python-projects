from random import shuffle
l = list()
for i in range(4):
    l.append(str(input(f"Nome do {i+1}o aluno: ")))
shuffle(l)
print("A ordem dos alunos que irão apresentar: ")
for i in range(len(l)):
    print(f"{i+1}o {l[i]}")
