from time import sleep


def msg(p):
    if p != "fim":
        print("\033[7;34m~"*(len(p)+4))
        print(f"{p:^{len(p)+4}}")
        print("\033[7;34m~"*(len(p)+4))
    else:
        print("\033[7;35m~" * (len(p) + 4))
        print(f"{p:^{len(p) + 4}}")
        print("\033[7;35m~" * (len(p) + 4))


def comando(f):
    sleep(1)
    print(f"\033[m\033[7;40m")
    print(help(f))


while True:
    msg("SISTEMA DE AJUDA PyHELP")
    f = str(input("\033[mFunção ou Biblioteca: ")).lower()
    if f == "fim":
        msg(f)
        break
    else:
        a = f"Acessando o manual do comando '{f}'"
        print("\033[7;33m~" * (len(a)+4))
        print(f"{a:^{len(a)+4}}")
        print("~" * (len(a)+4))
        comando(f)
