n = str(input("Digite o seu nome completo: ")).capitalize()
s = 0
for i in range(len(n.split())):
    if 'Silva' in n.split()[i].capitalize():
        s += 1
print(f"O nome completo de {n.split()[0]},")
if s >= 1:
    print("TEM 'Silva' no sobrenome.")
else:
    print("NÃO TEM 'Silva' no sobrenome.")
