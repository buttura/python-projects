n = str(input("Nome completo: "))
print(f"O primeiro nome: {n.split()[0]}")
if len(n.split()) >= 2:
    print(f"O último nome: {n.split()[len(n.split())-1]}")
