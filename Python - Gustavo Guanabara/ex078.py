l = list()
for i in range(5):
    n = int(input(f"Digite o {i+1}o valor: "))
    l.append(n)
ma = max(l)
me = min(l)
print(f"O maior valor digitado foi {ma} e está nas posições:", end=" ")
for i in range(len(l)):
    if l[i] == ma:
        print(f"{l.index(l[i])}...", end=" ")
        l[i] = ""
print(f"\nO menor valor digitado foi {me} e está nas posições:", end=" ")
for i in range(len(l)):
    if l[i] == me:
        print(f"{l.index(l[i])}...", end=" ")
        l[i] = ""
