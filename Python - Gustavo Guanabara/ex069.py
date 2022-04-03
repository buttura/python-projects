from datetime import date
c = h = m = 0
while True:
    a = int(input("Data de nascimento: "))
    a = date.today().year - a
    if a > 18:
        c += 1
    while True:
        s = str(input("Sexo: [M/F]")).strip().upper()[0]
        if s == "M" or s == "F":
            break
    if s == "F" and a < 20:
        m += 1
    if s == "M":
        h += 1
    while True:
        r = str(input("Deseja Continuar? [S/N] ")).upper().strip()[0]
        if r == "S" or r == "N":
            break
    if r == "N":
        break
print(f"Quantidade de pessoas que tem mais de 18 anos: {c}\n"
      f"Quantidade de homens que foram cadastrados: {h}\n"
      f"Quantidade de mulheres que tem menos de 20 anos: {m}")
