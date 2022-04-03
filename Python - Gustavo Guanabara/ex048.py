c = s = 0
for i in range(1, 500+1):
    if i % 2 != 0:
        if i % 3 == 0:
            c += 1
            s += i
print(f"A soma de todos os {c} valores solicitados é {s}")