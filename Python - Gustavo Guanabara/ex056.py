from datetime import date
idv = so = c = 0
nv = ""
for i in range(4):
    print(f"--=--= PESSOA {i+1} =--=--")
    n = str(input("Nome: "))
    while True:
        a = int(input("Ano de Nascimento: "))
        if 1900 <= a <= date.today().year:
            so += date.today().year - a
            break
    while True:
        s = str(input("Sexo: ")).upper()
        if s == "M" or s == "F":
            break
    if s == "M":
        if date.today().year - a > idv:
            idv = date.today().year - a
            nv = n
    if s == "F":
        if date.today().year - a < 20:
            c += 1
print(f"A média de idade do grupo: {so/4:.2f}\nO nome do homem mais velho: {nv}\nQuantidade de mulheres que tem menos de 20 anos: {c}")