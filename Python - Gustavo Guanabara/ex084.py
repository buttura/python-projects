lt = list()
l = list()
maior = menor = c = 0
while True:
    c += 1
    n = str(input("Digite o nome: "))
    lt.append(n)
    p = float(input("Digite o peso: "))
    lt.append(p)
    if c == 1:
        maior = menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
    l.append(lt[:])
    lt.clear()
    r = str(input("Deseja continuar? [S/N] "))[0]
    if r in "Nn":
        break
print(f"Ao todo, você cadastrou {len(l)} pessoas.\nO maior peso foi de {maior}Kg. Peso de", end=" ")
for i in range(len(l)):
    if l[i][1] == maior:
        print(f"[{l[i][0]}]", end=" ")
print(f"\nO menor peso foi de {menor}Kg. Peso de", end=" ")
for i in range(len(l)):
    if l[i][1] == menor:
        print(f"[{l[i][0]}]", end=" ")
