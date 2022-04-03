l = list()
for i in range(0, 2):
    l.append(int(input(f"[ {i+1} ] Digite um valor: ")))
print("--=--=--=--=--=--=--=--=--=--=--=--=")
while True:
    print("[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos Números\n[ 5 ] Sair do Programa")
    op = int(input("Sua opção: "))
    if op == 1:
        print(f"A soma entre os valores {l[0]} + {l[1]} = {l[0] + l[1]}")
    if op == 2:
        print(f"A multiplicação entre os valores {l[0]} x {l[1]} = {l[0]*l[1]}")
    if op == 3:
        if l[0] > l[1]:
            m = l[0]
        else:
            m = l[1]
        print(f"O maior valor é: {m}")
    if op == 4:
        l.clear()
        for x in range(0, 2):
            l.append(int(input(f"[ {x+1} ] Digite um valor: ")))
    if op == 5:
        break
    print("--=--=--=--=--=--=--=--=--=--=--=--=")
