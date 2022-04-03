d = dict()
g = list()
n = str(input("Nome do Jogador: "))
d["Nome"] = n
qp = int(input("Quantas partidas o jogador jogou? "))
for i in range(qp):
    g.append(int(input(f"Quantos gols fez na {i+1}o. partida? ")))
d["Gols"] = g
s = 0
print(f"O jogador {d['Nome']} jogou {qp} partidas.")
for i in range(len(d["Gols"])):
    print(f" => Na partida {i+1}, fez {d['Gols'][i]} gols.")
    s += d['Gols'][i]
print(f"Foi um total de {s} gols.")
