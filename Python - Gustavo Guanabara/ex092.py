d = dict()
from datetime import date
n = str(input("Digite o nome: "))
d["Nome"] = n
a = int(input("Ano de nascimento: "))
d["Idade"] = date.today().year - a
c = int(input("Carteira de trabalho: "))
if c != 0:
    d["Carteira de Trabalho"] = c
    ac = int(input("Ano de contratação: "))
    if 35 < d["Idade"]:
        d["Aposentar"] = f"aposentado há {d['Idade'] - 35} anos"
    else:
        d["Aposentar"] = 35 - d["Idade"]
    s = float(input("Salário: "))
    d["Salário"] = s
for c, v in d.items():
    print(f"{c} tem o valor {v}")