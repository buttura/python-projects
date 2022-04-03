d = dict()
l = list()
lgols = list()
while True:
    n = str(input("Nome do Jogador: "))
    q = int(input(f"Quantas partidas {n} jogou? "))
    for i in range(q):
        lgols.append(int(input(f"Quantos gols na {i+1}o. partida: ")))
    d["Nome"] = n
    d["Gols"] = lgols.copy()
    l.append(d.copy())
    lgols.clear()
    d.clear()
    r = str(input("Deseja continuar? [S/N] ")).strip()[0]
    if r in 'Nn':
        break
print(l)
s = 0
for i in range(len(l)):
    for x in range(len(l[i]['Gols'])):
        s += l[i]['Gols'][x]
    print(s)
    s = 0
while True:
    d = int(input("Mostrar dados de qual jogador? "))
    if d == 999:
        break
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {l[d]['Nome']}: ")
        for c, v in enumerate(l[d]['Gols']):
            print(f"No jogo {c+1}, fez {v} gols.")
