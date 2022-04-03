p = float(input("Digite o seu peso: "))
a = float(input("Digite a sua altura: "))
if p/(a**2) < 18.5:
    print("Abaixo do Peso")
elif 18.5 <= p/(a**2) <= 25:
    print("Peso Ideal")
elif 25 <= p/(a**2) <= 30:
    print("Sobrepeso")
elif 30 <= p/(a**2) <= 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")
