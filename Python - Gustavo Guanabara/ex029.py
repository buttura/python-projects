v = float(input("Velocidade do automóvel: "))
if v > 80:
    print(f"Você foi multado!\nA multa vai custar R${(v - 80)*7:.2f}")
else:
    print("Você não foi multado! Continue assim :)")