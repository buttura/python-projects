def ficha(n="", g=""):
    if n == "":
        n = "<desconhecido>"
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    print(f"O jogador {n} fez {g} gols(s) no campeonato.")


ficha(str(input("Nome do Jogador: ")).strip(), str(input("Número de gols:  ")).strip())
