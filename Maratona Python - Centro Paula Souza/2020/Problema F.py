while True:
    n = str(input())
    if len(n) == 11:
        break
l = list()
for i in range(0, len(n)):
    l.append(int(n[i]))
ver = l[9:]
del l[9:]
s = i = 0
for x in range(11-1, 1, -1):
    s += l[i] * x
    i += 1
v1 = 11 - (s % 11)
if v1 < 2:
    v1 = 0
l.append(v1)
s = i = 0
for x in range(12-1, 1, -1):
    s += l[i] * x
    i += 1
v2 = 11 - (s % 11)
if v2 < 2:
    v2 = 0
if v1 == ver[0] and v2 == ver[1]:
    print("Sim")
else:
    print("Não")
