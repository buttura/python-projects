s = c = menor = t = 0
nb = ""
while True:
    t += 1
    n = str(input("Nome do Produto: "))
    p = float(input("Preço do Produto: "))
    s += p
    if p > 1000:
        c += 1
    if t == 1:
        menor = p
        nb = n
    if p < menor:
        menor = p
        nb = n
    print("--=--=--=--=--=--=--=--=--=--=--==--")
    while True:
        r = str(input("Deseja Continuar? [S/N]"))
        if r == "S" or r == "N":
            break
    if r == "N":
        break
print(f"O total gasto da compra é R${s:.2f}\n"
      f"Quantidade de produtos que custam mais de R$1000: {c}\n"
      f"O nome do produto mais barato: {nb} e custa R${menor}")
