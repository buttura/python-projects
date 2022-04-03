p = int(input("Primeiro termo: "))
r = int(input("Razão: "))
res = 10
i = c = s = 10
while res != 0:
    while c != res:
        i += 1
        c += 1
        print(p + (i-1)*r, end="")
        print(", " if c != res else "", end="")
    res = int(input("\nDeseja mostrar quantos termos? [0 Encerra] "))
    s += res
    c = 0
print(f"Progressão finalizada com {s} termos mostrados.")
