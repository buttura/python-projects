val = list()
valtemp = list()
for l in range(0, 3):
    for c in range(0, 3):
        v = int(input(f"Digite um valor [{l}, {c}]: "))
        valtemp.append(v)
    val.append(valtemp[:])
    valtemp.clear()
print("--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--")
s = 0
stc = 0
for i in range(len(val)):
    for x in range(len(val[i])):
        print(f"[ {val[i][x]} ]", end=" ")
        if val[i][x] % 2 == 0:
            s += val[i][x]
    print("\n", end="")
    stc += val[i][2]
print("--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--")
print(f"A soma dos valores pares é {s}.")
print(f"A soma dos valores da terceira coluna é {stc}.")
print(f"O maior valor da segunda linha é {max(val[1])}.")