p = list()
i = list()
l = list()
while True:
    n = int(input("Digite um valor: "))
    l.append(n)
    if n % 2 == 0:
        p.append(n)
    else:
        i.append(n)
    r = str(input("Deseja continuar? [S/N] ")).strip()[0]
    if r in "Nn":
        break
print(f"A lista completa é {l}\nA lista de pares é {p}\nA lista de impares é {i}")
