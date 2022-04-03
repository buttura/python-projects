p = int(input("Primeiro termo: "))
r = int(input("Razão: "))
for i in range(1, 10+1):
    print(f"{p + (i-1)*r}", end="")
    print(", " if i < 10 else "", end="")
