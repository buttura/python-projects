f = str(input("Digite uma frase: ")).upper()
a = f.replace(" ", "")
p = ""
for i in range(1, len(a)+1):
    p += a[-i]
print(f"A frase: '{f}'", end=" ")
if a == p:
    print("é um palíndromo")
else:
    print("não é um palíndromo")
