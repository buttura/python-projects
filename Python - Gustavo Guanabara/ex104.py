def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print("\033[1;31m[ERRO!] Digite um número inteiro válido.\033[m")
    return n


n = leiaint("Digite um número: ")
print(f"Você acabou de digitar o número {n}")