t = ("América-MG", "Athletico-PR", "Atletico Goianiense", "Atlético Mineiro", "Avaí", "Botafogo", "Ceará",
     "Corinthians", "Cuiabá", "Flamengo", "Fluminense", "Fortaleza", "Goiás", "Internacional", "Juventude", "Palmeiras",
     "Bragantino", "Santos", "São Paulo")

a = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
print("Os primeiros cinco colocados:")
for i in range(5):
    print(i+1, t[i])
s = 20
print("--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--")
print("A posição dos últimos quatro colocados:")
for i in range(1, 5):
    print(s, t[-i])
    s -= 1
print("--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--")
print("A tabela do Campeonato brasileiro em ordem alfabética: ")
l = list()
for i in range(len(t)):
    for c, v in enumerate(l):
        if a.index(t[i][0]) < a.index(v[0]):
            l.insert(c, t[i])
            break
    else:
        l.append(t[i])
for i in range(len(l)):
    print(f"{l[i]}", end="")
    print(", " if i < len(l)-1 else "\n", end="")
print("--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--")
print("Tem Chapecoense no Campeonato Brasileiro?")
if "Chapecoense" in t:
    print(t.index("Chapecoense"))
else:
    print("Não tem Chapecoense na lista!")
