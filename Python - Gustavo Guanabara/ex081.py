s = 0
l = list()
while True:
    s += 1
    n = int(input(f"[ {s} ] Digite um valor: "))
    for c, v in enumerate(l):
        if n > v:
            l.insert(c, n)
            break
    else:
        l.append(n)
    r = str(input("Deseja continuar: [S/N] "))[0]
    if r in "Nn":
        break
s = 0
print(f"Foram digitados {len(l)} números.\nA lista ordenada de forma decrescente: {l}.")
for i in range(len(l)):
    if l[i] == 5:
        s += 1
if s >= 1:
    print("O valor cinco foi digitado na lista.")
else:
    print("O valor cinco NÃO foi digitado na lista.")
