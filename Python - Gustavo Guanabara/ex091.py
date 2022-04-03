from random import randint
from operator import itemgetter
d = dict()
print("Valores sorteados")
for i in range(4):
    d[f"Jogador{i}"] = randint(1, 6)
for c, v in d.items():
    print(f"O {c} tirou {v}")
ranking = list(sorted(d.items(), key=itemgetter(1), reverse=True))
print("Ranking dos Jogadores: ")
for c, v in enumerate(ranking):
    print(f"{c+1}o. lugar: {v[0]} com {v[1]}")