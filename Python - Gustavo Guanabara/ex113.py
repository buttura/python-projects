def leiaint(f):
    while True:
        try:
            v = int(input(f))
        except (ValueError, TypeError):
            print("\033[1;31mNúmero inválido, tente novamente!\033[m")
        except KeyboardInterrupt:
            print("\n\033[1;31mUsuário preferiu não digitar esse número.\033[m")
            v = 0
            break
        else:
            break
    return v


def leiafloat(f):
    while True:
        try:
            v = float(input(f))
        except (ValueError, TypeError):
            print("\033[1;31mNúmero inválido, tente novamente!\033[m")
        except KeyboardInterrupt:
            print("\n\033[1;31mUsuário preferiu não digitar esse número.\033[m")
            v = 0
            break
        else:
            break
    return v


a = leiaint("Digite um valor: [Inteiro] ")
b = leiafloat("Digite um valor: [Real] ")
print(f"O valor inteiro digitado foi {a} e o real foi {b}")
