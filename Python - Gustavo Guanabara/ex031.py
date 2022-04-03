d = float(input("Distância da viagem: [Km] "))
if d <= 200:
    print(f"Terá de pagar R${d*0.50:.2f}")
else:
    print(f"Terá de pagar R${d*0.45:.2f}")
