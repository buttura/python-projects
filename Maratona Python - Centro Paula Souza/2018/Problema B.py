from random import choice
g = list()
s = 0
res = list()
for i in range(0, 10):
    r = choice(["A", "B", "C", "D", "E"])
    g.append(r)
print(g)
while True:
    q = int(input("Quantidade de Alunos: "))
    if 1 <= q <= 50:
        break
for i in range(0, q):
    while True:
        r = str(input()).upper()
        if len(r) == len(g):
            break
    for x in range(0, len(g)):
        if r[x] == g[x]:
            s += 1
    res.append(f"{s} {s*10} {100-(s*10)}")
for i in range(0, len(res)):
    print(res)

