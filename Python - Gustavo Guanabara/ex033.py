l = list()
for i in range(0, 3):
    n = int(input(f"Digite o {i+1}o valor: "))
    for c, v in enumerate(l):
        if n < v:
            l.insert(c, n)
            break
    else:
        l.append(n)
print(f"O maior valor é: {l[len(l)-1]}\nO menor valor é: {l[0]}")
# OU
#v1 = int(input("Digite o primeiro valor: "))
#v2 = int(input("Digite o segundo valor: "))
#v3 = int(input("Digite o terceiro valor: "))
#print("O maior valor é: ", end="")
#if v2 < v1 > v3:
#    print(v1, end="\n")
#else:
#    if v1 < v2 > v3:
#        print(v2, end="\n")
#    else:
#        print(v3, end="\n")
#print("O menor valor é: ", end="")
#if v3 > v1 < v2:
#    print(v1)
#else:
#    if v3 > v2 < v1:
#        print(v2)
#    else:
#        print(v3)