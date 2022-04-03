from random import randint
c = 0
while True:
    while True:
        n = int(input("Diga um valor: "))
        if 0 <= n <= 10:
            break
    e = randint(0, 10)
    v = n + e
    pi = str(input("Par ou Impar? [P/I] ")).upper().strip()[0]
    print("--===--===--===--===--===--===--===--===--===--===--===--===--===--===--===")
    print(f"O computador pensou no número {e}, a soma entre os valores é {v}", end=" ")
    print("DEU PAR" if v % 2 == 0 else "DEU IMPAR")
    if v % 2 == 0 and pi == 'P' or v % 2 != 0 and pi == 'I':
        print("Você venceu!")
        c += 1
    else:
        print("Você perdeu")
        n = 0
        break
print("--===--===--===--===--===--===--===--===--===--===--===--===--===--===--===")
print(f"GAME OVER! Você venceu {c} vezes")

