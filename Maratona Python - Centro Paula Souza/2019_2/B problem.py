while True:
    c = int(input())
    if 1 <= c <= 1500:
        break
s = d = 0
dic = dict()
for i in range(c):
    while True:
        h = str(input())
        for x in range(1, len(h.split())):
            if 0 <= int(h.split()[x][:2]) <= 23 and 0 <= int(h.split()[x][3:5]) <= 59 and 0 <= int(h.split()[x][6:]) <= 59 and 1 <= int(h.split()[0]) <= c:
                s += 1
                d += int(h.split()[x][:2]) * 3600 + int(h.split()[x][3:5]) * 60 + int(h.split()[x][6:])
                dic[h.split()[0]] = d
        if s == len(h.split())-1:
            break
    s = 0
    d = 0
l = list()
for c, v in dic.items():
    for key, value in enumerate(l):
        if v < value:
            l.insert(key, v)
            break
    else:
        l.append(v)
print(l)
for i in range(len(l)):
    for k, v in dic.items():
        if l[i] == v:
            print(k)
            del dic[k]
            break
