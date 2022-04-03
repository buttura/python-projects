while True:
    d = int(input())
    if 1 <= d <= 180:
        break
s = m = c = ch = 0
for i in range(0, d):
    while True:
        s = 0
        b = str(input())
        for i in range(0, len(b.split())):
            if 1 <= int(b.split()[i]) <= 1000 and len(b.split()) == 3:
                s += 1
        if len(b.split()) == s:
            m += int(b.split()[0])
            c += int(b.split()[1])
            ch += int(b.split()[2])
            break

p = {"Milho verde": f"{int((m*200)/1000)}Kg", "Óleo vegetal": f"{int(((m*200) + (c*120) + (ch*240))/1000)}L",
     "Açúcar": f"{int(((m*250) + (c*360) + (ch*160))/1000)}Kg", "Fubá": f"{int((m*200)/1000)}Kg",
     "Ovos": f"{int((4*m) + (4*c) + (2*ch))}", "Farinha de trigo": f"{int(((m*15) + (c*240) + (ch*240))/1000)}Kg",
     "Coco ralado": f"{int(((m*15) + (c*100))/1000)}Kg", "Fermento em pó": f"{int(((m*5) + (c*10) + (ch*15))/1000)}Kg",
     "Leite de coco": f"{int((c*200)/1000)}L", "Chocolate em pó": f"{int((ch*90)/1000)}Kg", "Leite": f"{int((ch*240)/1000)}L"}
i = 0
for k, v in p.items():
    i += 1
    print(i, k, v)
