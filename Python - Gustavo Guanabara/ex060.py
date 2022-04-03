n = int(input("Digite um número: "))
print(f"{n}! =", end=" ")
i = n
while i != 0:
    print(i, end="")
    print(" x " if i > 1 else " = ", end="")
    i -= 1
    if i != 0:
        n *= i
print(n)