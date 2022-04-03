l = list()
for i in range(5):
    n = int(input(f"Digite o {i+1}o valor: "))
    for c, v in enumerate(l):
        if n < v:
            l.insert(c, n)
            print(f"Adicionado na posição {c} da lista...")
            break
    else:
        l.append(n)
        print("Adicionado ao final da lista...")
print(f"A lista ordenada:", end=" ")
for i in range(len(l)):
    print(l[i], end="")
    print("," if i < len(l)-1 else "", end=" ")