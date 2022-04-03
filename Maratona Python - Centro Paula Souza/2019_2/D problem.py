n = list()
no = list()
for l in range(0, 3):
    co = str(input(f"[{l}]: "))
    for i in range(len(co.split())):
        n.append(int(co.split()[i]))
    no.append(n[:])
    n.clear()
if (no[0][0] == -1 and no[0][1] == -1 and no[0][2] == -1) or (no[0][0] == -1 and no[1][0] == -1 and no[2][0] == -1) or (no[0][0] == -1 and no[1][1] == -1 and no[2][2] == -1) or (no[1][0] == -1 and no[1][1] == -1 and no[1][2] == -1) or (no[2][0] == -1 and no[2][1] == -1 and no[2][2] == -1) or (no[0][1] == -1 and no[1][1] == -1 and no[2][1] == -1) or (no[0][2] == -1 and no[1][2] == -1 and no[2][2] == -1) or (no[0][2] == -1 and no[1][1] == -1 and no[2][0] == -1):
    print("O")
else:
    if (no[0][0] == 1 and no[0][1] == 1 and no[0][2] == 1) or (no[0][0] == 1 and no[1][0] == 1 and no[2][0] == 1) or (no[0][0] == 1 and no[1][1] == 1 and no[2][2] == 1) or (no[1][0] == 1 and no[1][1] == 1 and no[1][2] == 1) or (no[2][0] == 1 and no[2][1] == 1 and no[2][2] == 1) or (no[0][1] == 1 and no[1][1] == 1 and no[2][1] == 1) or (no[0][2] == 1 and no[1][2] == 1 and no[2][2] == 1) or (no[0][2] == 1 and no[1][1] == 1 and no[2][0] == 1):
        print("X")
    else:
        print("Empate")
