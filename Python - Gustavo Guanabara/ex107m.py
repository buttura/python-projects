def leiafloat(n):
    while True:
        n = str(input(n))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print("Número inválido, tente novamente.", end=" ")
    return n


def aumentar(n, p=0):
    return n + n * p / 100


def diminuir(n, p=0):
    return n - n * p / 100


def metade(n):
    return n / 2


def dobro(n):
    return n * 2