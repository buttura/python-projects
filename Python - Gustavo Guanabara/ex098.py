def lin():
    print("--=--="*5)


def contador(i, f, p):
    q = s = 0
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f"Contagem de {i} até {f} de {p} em {p}")
    print(i, end=" ")
    if i < f:
        q = (f // p) - (i // p)
    else:
        q = (i // p) - (f // p)
    for c in range(q):
        if i < f:
            i += p
            print(i, end=" ")
        else:
            i -= p
            print(i, end=" ")
    print("FIM! \n", end="")

contador(1, 10, 1)
lin()
contador(10, 0, 2)
lin()
i = int(input("Início: "))
f = int(input("Fim:    "))
p = int(input("Passo:  "))
contador(i, f, p)
