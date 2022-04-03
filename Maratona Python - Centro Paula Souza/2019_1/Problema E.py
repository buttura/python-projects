nomes = ["João", "Pedro"]
escolha = ["pedra", "papel", "tesoura"]
lista = [[],[]]
s1 = s2 = 0
while True:
  j = int(input())
  if 1 <= j <= 1000:
    break
for i in range(0, j):
  for x in range(0, 2):
    while True:
      e = str(input())
      if e in escolha:
        break
    lista[x].append(e)
  if (lista[0][0] == "pedra" and lista[1][0] == "tesoura") or (lista[0][0] == "tesoura" and lista[1][0] == "papel") or  (lista[0][0] == "papel" and lista[1][0] == "pedra"):
    s1 += 1
  else:
    if (lista[1][0] == "pedra" and lista[0][0] == "tesoura") or (lista[1][0] == "tesoura" and lista[0][0] == "papel") or (lista[1][0] == "papel" and lista[0][0] == "pedra"):
      s2 += 1
  for a in range(0, 2):
    lista[a].clear()
if s1 > s2:
  print(f"{nomes[0]} {s1}")
else:
  if s2 > s1:
    print(f"{nomes[1]} {s2}")
  else:
    print("Empate")
