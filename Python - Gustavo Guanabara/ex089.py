notas = list()
ltemp = list()
l = list()
while True:
    n = str(input("Nome do aluno: "))
    for i in range(2):
        p = float(input(f"Nota da {i+1}o. prova: "))
        notas.append(p)
    ltemp.append(n)
    ltemp.append(notas[:])
    notas.clear()
    l.append(ltemp[:])
    ltemp.clear()
    r = str(input("Deseja continuar? [S/N]: "))
    if r in "Nn":
        break
m = 0
print("-"*40)
print(f"No. {'NOME':20} MÉDIA")
print("-"*40)
for i, a in enumerate(l):
    print(f"{i:<3} {a[0]:<22}", end="")
    for x in range(len(l[i][1])):
        m += a[1][x]
    print(f"{m/len(a[1]):>4.1f}", end="\n")
    m = 0
print("-"*40)
while True:
    a = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if a == 999:
        break
    else:
        print(f"Notas de {l[a][0]} são {l[a][1]}")
