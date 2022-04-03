def contador(i, f, p):
    print("-="*20)
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f"Contagem de {i} até {f} de {p} em {p}")
    if i < f:
        while i <= f:
            print(f"{i}", end=" ")
            i += p
    else:
        while i >= f:
            print(f"{i}", end=" ")
            i -= p
    print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input("Início: ")), int(input("Fim:    ")), int(input("Passo:  ")))