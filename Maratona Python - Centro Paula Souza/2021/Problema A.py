def MaS(n1, n2, n3):
  return (n1 + n2 + n3)/3


def MaP(n1, n2, n3):
  return (n1 * 5 + n2 * 3 + n3 * 2)/10

while True:
  while True:
    pa = str(input()).split()
    if pa[0] == 'A' or pa[0] == 'P' and 0 <= float(pa[1]) <= 10 and 0 <= float(pa[2]) <= 10 and 0 <= float(pa[3]) <= 10 or pa[0] == "0":
      break
  if pa[0] != "0":
    if pa[0] == 'A':
      print(f"{MaS(float(pa[1]), float(pa[2]), float(pa[3])):.2f}")
    else:
      print(f"{MaP(float(pa[1]), float(pa[2]), float(pa[3])):.2f}")
  else:
    break
