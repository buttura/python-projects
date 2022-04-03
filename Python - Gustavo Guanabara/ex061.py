p = int(input("Primeiro termo: "))
r = int(input("Razão: "))
i = 0
while i != 10:
    i += 1
    print(p + (i-1)*r, end="")
    print(", " if i != 10 else "", end="")
