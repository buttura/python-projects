from random import randint
from time import sleep
print("Vou pensar em um número entre 0 e 5. Tente Adivinhar...")
while True:
    n = int(input("Em que número eu pensei? "))
    if 0 <= n <= 5:
        break
print("PROCESSANDO...")
sleep(1)
if n == randint(0, 5):
    print("Parabéns! Você conseguiu me vencer!")
else:
    print("Você não conseguiu me vencer! HAHAHAHA!")