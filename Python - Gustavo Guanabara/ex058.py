from random import randint
p = 1
while True:
    s = int(input("Digite um número: "))
    if s == randint(0, 10):
        break
    else:
        print("Tente novamente,", end=" ")
        p += 1
print(f"Parabéns! Você acertou! Foram necessários {p} palpites.")
# Ou
#s = 1
#n = int(input("Digite um número: "))
#while randint(0, 10) != n:
#    n = int(input("Tente novamente, digite um número: "))
#    s += 1
#print(f"Parabéns! Você acertou! Foram necessários {s} palpites.")