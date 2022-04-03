from random import choice
l = ["pedra", "papel", "tesoura"]
s = 0
d = {"Jogador":0, "Computador":0}
q = int(input("Quantidade de partidas: "))
for i in range(q):
    while True:
        j = str(input("Sua jogada: ")).lower().strip()[:2]
        for i in range(len(l)):
            if j in l[i][:2]:
                s += 1
        if s == 1:
            break
    s = 0
    if j == "pe":
        j = "pedra"
    elif j == "pa":
        j = "papel"
    else:
        j = "tesoura"
    e = choice(l)
    print("--=--=--=--=--=--=--=--=--=--")
    print(f"O computador pensou: {e}")
    print(f"{j} x {e}")
    print("--=--=--=--=--=--=--=--=--=--")
    if (j == "pedra" and e == "tesoura") or (j == "papel" and e == "pedra") or (j == "tesoura" and e == "papel"):
        d["Jogador"] += 1
    elif (e == "pedra" and j == "tesoura") or (e == "papel" and j == "pedra") or (e == "tesoura" and j == "papel"):
        d["Computador"] += 1
    else:
        d["Computador"] += 1
        d["Jogador"] += 1
if d["Computador"] > d["Jogador"]:
    print(f"Você perdeu! [{d['Jogador']} x {d['Computador']}]")
elif d["Computador"] < d["Jogador"]:
    print(f"Você ganhou! [{d['Jogador']} x {d['Computador']}]")
else:
    print(f"Empate [{d['Jogador']} x {d['Computador']}]")
