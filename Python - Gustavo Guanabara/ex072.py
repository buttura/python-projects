n = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze",
     "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
c = 0
while True:
    num = int(input("Digite um número [0 até 20]: "))
    if 0 <= num <= 20:
        break
    else:
        c += 1
        print(f"({c}) Tente novamente.", end="")
print(f"Você digitou o número {n[num]}")
