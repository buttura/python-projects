def linha(tam=42):
    return "-" * tam


def cabecalho(msg):
    print(linha(42))
    print(f"{msg:^42}")
    print(linha(42))


def leiaint(f):
    while True:
        try:
            v = int(input(f))
        except (ValueError, TypeError):
            print("\033[1;32mERRO: Digite um número válido!\033[m")
        except KeyboardInterrupt:
            print("\033[1;32mUsuário preferiu não informar\033[m")
            return 0
        else:
            return v


def menu(lista):
    c = 1
    cabecalho("MENU PRINCIPAL")
    for k, v in enumerate(lista):
        print(f"\033[1;33m{c}\033[m - \033[1;32m{v}\033[m")
        c += 1
    print(linha())
    opc = leiaint("\033[36mSua opção: \033[m")
    return opc