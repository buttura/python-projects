while True:
    xy = str(input())
    if len(xy.split()) == 2 and 1 <= int(xy.split()[0]) <= 30 and 1 <= int(xy.split()[1]) <= 100:
        break
l = list()
for i in range(int(xy.split()[0])):
    l.append("L")
for x in range(int(xy.split()[1])):
    while True:
        n = int(input())
        if 1 <= n <= int(xy.split()[0]):
            break
    c = n
    for i in range(n):
        if c == 0:
            break
        if n % c == 0:
            if l[c-1] == 'D':
                l[c-1] = 'L'
            else:
                l[c-1] = 'D'
        c -= 1
print(l)
