from random import randint
while True:
  j = int(input("Quantidade de jogadas: "))
  if 1 <= j <= 100:
    break
l = [[],[]]
s = 0
ns = ["Adam", "Ana"]
m = ["cara", "coroa"]
for x in range(0, j):
  for i in range(0, 2):
    while True:
      jo = str(input(f"Jogada [{ns[i]}]: ")).strip().lower()
      if jo == m[0] or jo == m[1]:
        break
    c = randint(0, 1)
    if m[c] == jo:
      l[i].append(ns[i])
      s += 1
if len(l[0]) > len(l[1]):
  print(f"{ns[0]} {s}")
else:
  if len(l[1]) > len(l[0]):
    print(f"{ns[1]} {s}")
  else:
    print("Empate")
