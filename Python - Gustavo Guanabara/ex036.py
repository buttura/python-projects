v = float(input("Valor da Casa: R$"))
s = float(input("Salário: "))
a = int(input("Quantos anos deseja pagar? "))
if v/a/12 > s * 30/100:
    print(f"O valor da prestação mensal da casa é: R${v/a/12:.2f}\nO empréstimo será negado")
else:
    print(f"O empréstimo está aceito, portanto, o valor da prestação da casa é R${v/a/12:.2f}")
