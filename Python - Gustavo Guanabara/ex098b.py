from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print("-=" * 20)
    sleep(1)
    print(f"Contagem de {i} até {f} de {p} em {p}")
    if i < f:
        c = i
        while c <= f:
            print(f"{c}", end=" ")
            sleep(0.2)
            c += p
    else:
        c = i
        while c >= f:
            print(f"{c}", end=" ")
            sleep(0.2)
            c -= p
    print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)
print("-=" * 20)
print("Agora é sua vez de personalizar a contagem!")
contador(int(input("Início: ")), int(input("Fim:    ")), int(input("Passo:  ")))
