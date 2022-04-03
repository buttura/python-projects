d = dict()
Nome = str(input("Nome: ")).strip()
while True:
    Media = float(input(f"Média de {Nome}: "))
    if 0 <= Media <= 10:
        break
d["Nome"] = Nome
d["Média"] = Media
if d["Média"] >= 7:
    d["Situacao"] = "Aprovado"
else:
    if 5 <= d["Média"] < 7:
        d["Situacao"] = "Recuperação"
    else:
        d["Situacao"] = "Reprovado"
for k, v in d.items():
    print(f"{k} é igual a {v}")
