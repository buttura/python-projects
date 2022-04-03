from math import sqrt, pow
co = float(input("Digite o comprimento do Cateto Oposto: "))
ca = float(input("Digite o comprimento do Cateto Adjascente: "))
#print(f"O comprimento da hipotenusa é {(co**2 + ca**2)**(1/2):.2f}")
# OU
print(f"O comprimento da hipotenusa é {sqrt(pow(co, 2) + pow(ca, 2)):.2f}")