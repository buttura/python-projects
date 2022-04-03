while True:
    x = int(input())
    if 3 <= x <= 100:
        break
s = 0
while True:
    a = str(input())
    for i in range(len(a.split())):
        if a.split().count(a.split()[i]) < 2:
            s += 1
    if s == len(a.split()) <= x-1:
        break
    else:
        s = 0
l = list(range(1, x+1))
for i in range(len(l)):
    if str(l[i]) not in a.split():
        print(l[i])
