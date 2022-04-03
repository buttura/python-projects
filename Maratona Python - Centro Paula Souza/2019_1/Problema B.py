ganhadores = dict()
valores = list()
for i in range(0, 1):
    while True:
        n = int(input())
        if 1 <= n <= 2135:
            break
    while True:
        d = str(input())
        if 1 <= int(d[:2]) <= 31 and 1 <= int(d[3:5]) <= 12 and 2009 <= int(d[6:]) <= 2019:
            if (int(d[6:]) == 2009 and int(d[3:5]) >= 5 and int(d[:2]) >= 27) or (int(d[6:]) == 2019 and int(d[3:5]) <= 3 and int(d[:2]) <= 30) or (2010 <= int(d[6:]) <= 2018):
                break
    while True:
        g = int(input())
        if 1 <= g <= 5:
            break
    c = str(input()).lower()
    while True:
        e = str(input()).upper()
        if len(e) == 2:
            break
    while True:
        v = float(input())
        if 729819.96 <= v <= 205329753.89:
            break
    c += f" {e}"
    if c not in ganhadores:
        ganhadores[c] = v
    else:
        s = v
        ganhadores[c] += s
    s = 0
for k in ganhadores.keys():
    valores.append(ganhadores[k])
valores.sort(reverse=True)
if len(valores) < 3:
    for i in range(0, len(valores)):
        for k, v in ganhadores.items():
            if valores[i] == ganhadores[k]:
                print(f"{k} {v}")
else:
    for i in range(0, 3):
        for k, v in ganhadores.items():
            if valores[i] == ganhadores[k]:
                print(f"{k} {v}")
