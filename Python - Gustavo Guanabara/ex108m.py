def leiafloat(n):
    a = n
    while True:
        v = False
        n = str(input(a))
        for i in range(len(n)):
            if n[i] == "." or n[i] == ",":
                v = True
                break
        if v or n.isnumeric():
            n = n.replace(",", ".")
            n = float(n)
            break
        else:
            print("Número inválido, tente novamente.", end=" ")
    return n


def moeda(n, moeda="R$"):
    #n = f"{n:.2f}"
    #l = list()
    #for i in range(len(n)):
    #    l.append(n[i])
    #for i in range(len(l)):
    #    if l[i] == ".":
    #        l[i] = ","
    #f = f"{moeda}"
    #for i in range(len(l)):
    #    f += l[i]
    #return f"{f}"
    # OU
    if "." in str(n):
        return f"{moeda}{n:>.2f}".replace(".", ",")
    else:
        return f"{moeda}{n:>.2f}".replace(",", ".")



def aumentar(n, p=0):
    return n + n * p / 100


def diminuir(n, p=0):
    return n - n * p / 100


def metade(n):
    return n / 2


def dobro(n):
    return n * 2
