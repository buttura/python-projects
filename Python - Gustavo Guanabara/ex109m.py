def leiafloat(f):
    a = f
    v = False
    while True:
        n = str(input(a))
        for i in range(len(n)):
            if n[i] == "." or n[i] == ",":
                v = True
                break
        if n.isnumeric() or v:
            n = n.replace(",", ".")
            n = float(n)
            break
    return n


def moeda(n, m="R$"):
    return f"{m}{n:.2f}".replace(".", ",")


def dobro(n, f=False):
    return n * 2 if f is False else moeda(n*2)


def metade(n, f=False):
    return n / 2 if f is False else moeda(n/2)


def aumentar(n, p, f=False):
    return n + n * p / 100 if f is False else moeda(n + n * p / 100)


def diminuir(n, p, f=False):
    return n - n * p / 100 if f is False else moeda(n + n * p / 100)


