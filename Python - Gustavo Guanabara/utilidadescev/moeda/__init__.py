def moeda(n, m="R$"):
    return f"{m}{n:.2f}".replace(".", ",")


def dobro(n, f=False):
    return n * 2 if f is False else moeda(n*2)


def metade(n, f=False):
    return n / 2 if f is False else moeda(n/2)


def aumentar(n, a, f=False):
    return n + n * a / 100 if f is False else moeda(n + n * a / 100)


def diminuir(n, r, f=False):
    return n - n * r / 100 if f is False else moeda(n - n * r / 100)


def lin():
    print("-"*30)


def resumo(n, a, r):
    lin()
    print(f"{'RESUMO DO VALOR':^30}")
    lin()
    print(f"Preço analisado: {moeda(n)}")
    print(f"Metade do preço: {metade(n, f=True)}")
    print(f"Dobro do preço: {dobro(n, f=True)}")
    print(f"{a}% de aumento: {aumentar(n, a, f=True)}")
    print(f"{r}% de redução: {diminuir(n, r, f=True)}")
