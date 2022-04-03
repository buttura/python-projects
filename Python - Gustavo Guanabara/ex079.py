l = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in l:
        for c, v in enumerate(l):
            if n < v:
                l.insert(c, n)
                break
        else:
            l.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar")
    r = str(input("Quer continuar? [S/N] "))[0]
    if r in "Nn":
        break
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Você difitou os valores: ")
for i in range(len(l)):
    print(l[i], end="")
    print(", " if i < len(l)-1 else "", end="")
