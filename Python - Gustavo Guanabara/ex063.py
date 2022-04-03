n = int(input("Quantos termos você quer mostrar: "))
contador = a = 0
b = c = 1
while contador != n:
    contador += 1
    print(a, end="")
    print(" -> " if contador != n else "", end="")
    a = b
    b = c
    c = b + a
