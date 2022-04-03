n = float(input("Digite um valor a ser sacado: R$"))
print("Serão necessários: ")
while True:
    if n >= 50:
        print(f"{n//50} cédulas de R$50", end="\n")
        n -= (n//50 * 50)
    if n >= 20:
        print(f"{n//20} cédulas de R$20", end="\n")
        n -= (n//20 * 20)
    if n >= 10:
        print(f"{n//10} cédulas de R$10", end="\n")
        n -= (n//10 * 10)
    if n >= 1:
        print(f"{n//1} cédulas de R$1", end="\n")
        n -= (n//1 * 1)
    if n == 0:
        break
