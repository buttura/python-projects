while True:
  q = int(input())
  if 1 <= q <= 100:
    break
l = list()
for i in range(q):
  while True:
    s = 0
    p = str(input()).strip().lower()
    l.append(p.split())
    if "lona" in l[i]:
      l[i][l[i].index("lona")] = "0"
    for x in range(2, len(l[i])):
      if 0 <= int(l[i][x]) <= 10:
        s += 1
    if s == 2 and len(l[i]) == 4:
      break
    else:
      l[i].clear()
      s = 0
s = j = f = 0
for i in range(len(l)):
  for x in range(len(l[i])-2):
    s += len(l[i][x])
  if str(s) in l[i]:
    if l[i].index(str(s)) == 2:
      j += 1
    else:
      f += 1
  s = 0
if j > f:
  print("Jilo")
else:
  if j < f:
    print("Ferrugem")
  else:
    print("Empate")
