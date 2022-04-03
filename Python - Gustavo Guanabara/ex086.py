valores = list()
valores_temporarios = list()
for l in range(0, 3):
    for c in range(0, 3):
        v = int(input(f"Digite um valor para [{l},{c}]: "))
        valores_temporarios.append(v)
    valores.append(valores_temporarios[:])
    valores_temporarios.clear()
for i in range(len(valores)):
    for x in range(len(valores[i])):
        print(f"[ {valores[i][x]} ]", end=" ")
    print("\n", end="")