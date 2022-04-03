a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
     "X", "Y", "Z"]
while True:
    c = str(input()).upper()
    if 1 <= len(c) <= 50:
        break
for i in range(len(c)):
    if c[i] in a:
        if a.index(c[i])+3 > len(a):
            print(a[a.index(c[i])]-len(a)+3, end="")
        else:
            print(a[a.index(c[i])+3], end="")
    else:
        print("", end=" ")
