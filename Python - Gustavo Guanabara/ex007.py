from math import ceil
l = list()
for i in range(0, 2):
    while True:
        l.append(float(input(f"{i+1}o nota do aluno: ")))
        if 0 <= l[i] <= 10:
            break
s = 0
for i in range(len(l)):
    s += l[i]
print(f"A média entre {l[0]} e {l[1]} é igual a {s/len(l):.1f}")