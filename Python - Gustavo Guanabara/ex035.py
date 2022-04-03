l = list()
for i in range(3):
    l.append(float(input(f"Digite o {i + 1}o lado do triângulo: ")))
if (l[0] + l[1]) > l[2] and (l[0] + l[2]) > l[1] and (l[1] + l[2]) > l[0]:
    if l[0] == l[1] == l[2]:
        print("Triângulo Equilátero")
    else:
        if l[2] != l[0] == l[1] or l[1] != l[0] == l[2] or l[0] != l[1] == l[2]:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
else:
    print("Não é possível formar um triângulo")
