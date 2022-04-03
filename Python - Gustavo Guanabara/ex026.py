f = str(input("Frase: ")).lower()
l = list()
if 'a' in f:
    print(f"Quantidade de vezes que aparece a Letra A na frase: {f.count('a')}"
          f"\nA posição em que a letra A aparece pela primeira vez: {f.index('a')}")
    if f.count('a') >= 2:
        print("A posição em que a letra A aparece na última vez: {f.rindex('a')}")
else:
    print("Não tem a letra A na frase")
