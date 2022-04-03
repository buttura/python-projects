q = int(input())
l = list()
for _ in range(q):
    t = 0
    while True:
        n = int(input())
        if 1 <= n <= 2305:
            break
    d = str(input())
    while True:
        dz = str(input())
        for i in range(len(dz.split())):
            if 1 <= int(dz.split()[i]) <= 60:
                t += 1
        if (len(dz.split()) == 6) and (t == 6):
            for i in range(len(dz.split())):
                for c, v in enumerate(l):
                    if int(dz.split()[i]) < v:
                        l.insert(c, int(dz.split()[i]))
                        break
                else:
                    l.append(int(dz.split()[i]))
            break
        else:
            t = 0
d = dict()
for i in range(len(l)):
    if i < len(l)-1:
        if l[i] == l[i + 1]:
            i -= 2
        else:
            d[l[i]] = l.count(l[i])
    else:
        d[l[i]] = l.count(l[i])
i = 0
for k, v in d.items():
    i += 1
    print(i, k, v)