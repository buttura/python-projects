_ = 0
while True:
    # O m vai pegar as linhas e as colunas, depois vai ter uma verificação
    m = str(input("[L] & [C]: ")).upper()
    for i in range(len(m.split())):
        if 1 <= int(m.split()[i]) <= 100:
            _ += 1
    if _ == len(m.split()):
        break
    else:
        _ = 0
_ = 0
li = list()
# A lista li vai armazenar a parte do navio e a agua, depois vai ter uma verificação
while True:
    for l in range(int(m.split()[0])):
        xa = str(input("XA: "))
        if len(xa) == int(m.split()[1]):
            li.append(xa)
            _ += 1
    if _ == int(m.split()[0]):
        break
    else:
        li.clear()
        _ = 0
of = list()
of.append(li[:])
# A lista of vai pegar uma cópia da lista li, pois a lista li vai ser usada para armazenar as coordenadas dos tiros
li.clear()
n = list()
# Vai pegar as coordenadas e armazenar na lista li, depois o n vai pegar a cópia da lista li
for i in range(int(m.split()[0])):
    while True:
        t = str(input())
        if len(t.split()) == 2:
            break
    for x in range(len(t.split())):
        li.append(int(t.split()[x]))
    n.append(li[:])
    li.clear()
print(of)
print(of[0])
print(n)
# Vai verificar se aquelas coordenadas contém o X, se caso sim "Acertou", senão, "Agua"
for i in range(len(of[0])):
    # Dentro da lista of (Onde estão armazenadas as partes do navio e X), vai pegar a coordenada da linha e depois
    # A coordenada da coluna dentro da lista of e vai verificar se aquele valor é igual a "X" de acordo com as
    # coordenadas
    if of[0][n[i][0]-1][n[i][1]-1] == "X":
        print("acertou")
    else:
        print("agua")
