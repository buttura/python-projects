l = list()
while True:
    for i in range(3):
        l.append(float(input(f"{i+1}o lado do Triângulo: ")))
    if l[0] + l[1] > l[2] and l[1] + l[2] > l[0] and l[0] + l[2] > l[1]:
        if l[0] == l[1] == l[2]:
            print("Triângulo Equilátero")
            break
        elif l[0] == l[1] < l[2] or l[0] == l[2] < l[1] or l[1] == l[2] < l[0]:
            print("Triângulo Isósceles")
            break
        else:
            print("Triângulo Escaleno")
            break
    else:
        print("É impossível formar um triângulo com esses lados!")
        l.clear()
