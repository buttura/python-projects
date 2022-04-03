from random import randint
from time import sleep
q = int(input("Quantos jogos você quer jogar? "))
ltemp = list()
l = list()
for i in range(q):
    for x in range(6):
        ltemp.append(randint(1, 60))
    l.append(ltemp[:])
    ltemp.clear()
for i in range(len(l)):
    sleep(1)
    print(f"JOGO {i+1}: {l[i]}")