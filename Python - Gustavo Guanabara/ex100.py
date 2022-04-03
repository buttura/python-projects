from random import randint
from time import sleep
numeros = list()


def sorteia(n):
    print("Sorteando 5 valores da lista:", end=" ")
    for i in range(5):
        e = randint(0, 10)
        n.append(e)
        sleep(0.5)
        print(e, end=" ")
    print("PRONTO!")


def somapar(n):
    print(f"Somando os valores pares de {n},", end=" ")
    s = 0
    for v in n:
        if v % 2 == 0:
            s += v
    print(f"temos {s}")


sorteia(numeros)
somapar(numeros)
