l = [[], []]
for i in range(7):
    n = int(input(f"Digite o {i+1}o. valor: "))
    if n % 2 == 0:
        for c, v in enumerate(l[0]):
            if n < v:
                l[0].insert(c, n)
                break
        else:
            l[0].append(n)
    else:
        for c, v in enumerate(l[1]):
            if n < v:
                l[1].insert(c, n)
                break
        else:
            l[1].append(n)
print(f"Os valores pares digitados foram: {l[0]}\nOs valores ímpares digitados foram: {l[1]}")
