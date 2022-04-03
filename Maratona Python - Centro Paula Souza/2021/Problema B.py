alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

frase = str(input("Frase: ")).upper()
for i in range(0, len(frase)):
  if frase[i] in alfabeto:
    if alfabeto.index(frase[i])+3 > len(alfabeto):
      print(alfabeto[alfabeto.index(frase[i])-len(alfabeto)+3], end="")
    else:
      print(alfabeto[alfabeto.index(frase[i])+3], end="")
  else:
    print("", end=" ")
