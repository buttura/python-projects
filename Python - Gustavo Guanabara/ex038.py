l = list()
for i in range(2):
    n = int(input(f"Digite o {i+1}o valor: "))
    for c, v in enumerate(l):
        if n < v:
            l.insert(c, n)
            break
    else:
        l.append(n)
if l[0] == l[1]:
    print("Não existe valor maior, os dois são iguais!")
else:
    print(f"O valor {l[1]} é o maior\nO valor {l[0]} é o menor")
