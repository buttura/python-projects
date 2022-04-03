while True:
    s = str(input("Sexo: [M/F]")).strip().upper()[0]
    if s == "M" or s == "F":
        break
    else:
        print("Dados inválidos, por favor digite o seu", end=" ")
if s == "M":
    s = "Masculino"
else:
    s = "Feminino"
print(f"Sexo {s} registrado com sucesso!")
# Ou
#sexo = str(input("Sexo: [M/F] "))
#while sexo not in 'MmFf':
#    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: [M/F] "))