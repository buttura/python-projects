r = ""
c = s = maior = menor = 0
while r != "N":
    n = int(input(f"[ {c+1} ] Digite um valor: "))
    c += 1
    s += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input("Deseja continuar: [S/N] ")).upper().strip()[0]
print(f"A média entre todos os valores é {s/c:.2f}\nO maior valor lido é: {maior}\nO menor valor lido é: {menor}")
