t = (int(input("Digite o primeiro valor: ")), int(input("Digite o segundo valor: ")),
     int(input("Digite o terceiro valor: ")), int(input("Digite o quarto valor: ")))
if 9 in t:
    print(f"O número nove apareceu {t.count(9)} vezes")
else:
    print("Não tem nove na tupla")
if 3 in t:
    print(f"A posição em que o número três aparece: {t.index(3)}")
else:
    print("Não tem número três na lista")
s = 0
for i in range(len(t)):
    if t[i] % 2 == 0:
        s += 1
if s >= 1:
    print("Os números pares foram:", end=" ")
    for i in range(len(t)):
        if t[i] % 2 == 0:
            print(t[i], end="")
            print(", " if i < s-1 else "", end="")
else:
    print("Não tem número par na tupla")