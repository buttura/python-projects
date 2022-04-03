while True:
    t = int(input())
    if 1 <= t <= 500:
        break
l = list()
of = list()
for i in range(0, t):
    n = int(input())
    if n >= 50:
        o50 = int(n//50)
        l.append(o50)
        n -= (o50 * 50)
    else:
        l.append(int(n//50))
    if n >= 10:
        p10 = int(n//10)
        l.append(p10)
        n -= (p10 * 10)
    else:
        l.append(int(n//10))
    if n >= 5:
        q5 = int(n//5)
        l.append(q5)
        n -= (q5 * 5)
    else:
        l.append(int(n//5))
    if n < 5:
        r1 = int(n//1)
        l.append(r1)
        n -= (r1 * 1)
    else:
        l.append(int(n//1))
    of.append(l[:])
    l.clear()
for i in range(0, len(of)):
    print(f"Caso de Teste {i+1}: ", end="")
    for x in range(0, len(of[i])):
        print(of[i][x], end=" ")
    print("\n",end="")
