s = float(input("Salário do Funcionário: R$"))
if s > 1250:
    print(f"O seu salário é SUPERIOR, portanto terá um aumento de 10%\nFicando assim, R${s + s*10/100:.2f}")
else:
    print(f"O seu salário é INFERIOR, portanto terá um aumento de 15%\nFicando assim, R${s + s * 15/100:.2f}")