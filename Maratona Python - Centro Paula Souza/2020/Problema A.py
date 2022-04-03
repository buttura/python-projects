v = ["A", "E", "I", "O", "U"]
s = 0
while True:
    n = str(input()).upper()
    for i in range(len(n.split())):
        if len(n.split()[i]) >= 3:
            s += 1
    if 1 <= len(n.split()) <= 30 and s == len(n.split()):
        break
    else:
        s = 0
s = 0
vp = list()
vs = list()
vstemp = list()
for i in range(len(n.split()[0])):
    if n.split()[0][i] in v:
        vp.append(n.split()[0][i])
for i in range(len(n.split())):
    for x in range(len(n.split()[i])):
        if n.split()[i][x] in v:
            vstemp.append(n.split()[i][x])
    vs.append(vstemp[:])
    vstemp.clear()
mv = list()
for i in range(1, len(vs)):
    p = 0
    for x in range(len(vs[i])):
        if vs[i][x] in vp:
            if vs[i].count(vs[i][x]) > vp.count(vs[i][x]):
                p += 1
                mv.append(vs[i][x])
        if vs[i][x] not in vp:
            s -= 1
        if p == 1 and mv[0] == vs[i][x]:
            s -= 1
    s += 1
print(s)
