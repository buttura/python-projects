while True:
    while True:
        q = int(input())
        if 0 <= q <= 1000:
            break
    if q != 0:
        l = list()
        s = 0
        a = ""
        for i in range(q):
            while True:
                s = 0
                a = str(input()).upper().split()
                for c in range(2, len(a)):
                    if a[c] == "LONA" or 0 <= int(a[c]) <= 10:
                        s += 1
                if (s == 2 and a[2] != a[3]) or (a[0] == "0"):
                    break
            if a[0] == '0':
                break
            l.append(a)
            if "LONA" in l[i]:
                l[i][l[i].index("LONA")] = "0"
            for x in range(len(l[i])):
                if l[i][x].isnumeric():
                    l[i][x] = int(l[i][x])
        if a[0] != '0':
            n = dict()
            n["Jilo"] = 0
            n["Ferrugem"] = 0
            for i in range(len(l)):
                p = 0
                for x in range(len(l[i])):
                    if type(l[i][x]) == str:
                      p += l[i][x].count("I")
                if p in l[i]:
                    if l[i].index(p) % 2 == 0:
                        n["Jilo"] += 1
                    else:
                        n["Ferrugem"] += 1
            if n["Jilo"] > n["Ferrugem"]:
                print("Jilo")
            else:
                if n["Jilo"] < n["Ferrugem"]:
                    print("Ferrugem")
                else:
                    print("Empate")
    else:
        break
