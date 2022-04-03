def leiafloat(f):
    v = False
    while True:
        l = list()
        n = str(input(f))
        if "." in n or "," in n:
            v = True
        if n.isnumeric() or v:
            n = float(n)
            break
        else:
            l.clear()
            print("Número inválido, tente novamente.", end=" ")
    return n


def metade(n, f=True):
    return n/2 if f is False else moeda(n/2)


def dobro(n, f=True):
    return n*2 if f is False else moeda(n*2)


def moeda(n, m="R$"):
    return f"{m}{n:.2f}".replace(".", ",")


def aumentar(p, a, f=True):
    return p + p * a / 100 if f is False else moeda(p + p * a / 100)


def diminuir(p, a, f=True):
    return p - p * a / 100 if f is False else moeda(p - p * a / 100)


def lin():
    return print("-"*30)


def resumo(n, a, r):
    lin()
    print(f"{'RESUMO DO VALOR':^30}")
    lin()
    print(f"Preço analisado: {moeda(n)}")
    print(f"Metade do preço: {metade(n, f=True)}")
    print(f"Dobro do preço: {dobro(n, f=True)}")
    print(f"{a}% de aumento: {aumentar(n, a, f=True)}")
    print(f"{r}% de redução: {diminuir(n, r, f=True)}")
    lin()
