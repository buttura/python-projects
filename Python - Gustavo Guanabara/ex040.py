l = list()
for i in range(2):
    while True:
        n = float(input(f"{i+1}o nota: "))
        if 0 <= n <= 10:
            l.append(n)
            break
if (l[0] + l[1])/len(l) < 5:
    print("REPROVADO")
elif 5 <= (l[0] + l[1])/len(l) < 7:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
