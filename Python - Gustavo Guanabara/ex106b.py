from time import sleep
cores = ("\033[m",         # 0 - sem cores
     "\033[0;30;41m",  # 1 - vermelho
     "\033[0;30;42m",  # 2 - verde
     "\033[0;30;43m",  # 3 - amarelo
     "\033[0;30;44m",  # 4 - azul
     "\033[0;30;45m",  # 5 - roxo
     "\033[7;30m"      # 6 - branco
     )


def ajuda(c, cor=0):
    titulo(f"Acessando o manual do comando '{c}'", 4)
    print(cores[cor], end="")
    print(help(c))
    print(cores[0], end="")
    sleep(2)


def titulo(msg, cor=0):
    print(cores[cor], end="")
    print("~" * (len(msg)+4))
    print(f"{msg:^{len(msg)+4}}")
    print("~" * (len(msg)+4))
    print(cores[0], end="")
    sleep(1)


while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando, 6)
titulo("ATÉ LOGO!", 1)
