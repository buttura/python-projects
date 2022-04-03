from math import ceil
p = c = v = 0
while True:
    a = int(input("Altura do Tijolo: "))
    if a == 0:
        break
    if 5 <= a <= 20:
        break
if a != 0:
    while True:
        l = int(input("Largura do Tijolo: "))
        if l == 0:
            break
        if 5 <= l <= 20:
            break
    if l != 0:
        while True:
            c = int(input("Comprimento do Tijolo: "))
            if c == 0:
                break
            if 0 <= c <= 50:
                break
        if c != 0:
            while True:
                p = int(input("Perímetro do Cômodo: "))
                if p == 0:
                    break
                if 8 <= p <= 200:
                    break
            if p != 0:
                while True:
                    v = int(input("Valor: R$"))
                    if v == 0:
                        break
                    if 50 <= v <= 2670:
                        break
                if v != 0:
                    tm2 = int(1/((c/100 + 0.01) * (a/100 + 0.01)))
                    q = ceil(tm2 * p * 2.8)
                    vt = int((v*q)/1000)
                    print(f"{tm2} {q} {vt}")
