maior = menor = 0
for i in range(5):
    print(f"--=--= PESSOA {i+1} =--=--")
    p = float(input("Peso: "))
    if i == 0:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f"O menor peso: {menor}Kg\nO maior peso: {maior}Kg")