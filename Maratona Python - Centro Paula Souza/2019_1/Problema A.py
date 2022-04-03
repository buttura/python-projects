while True:
    lt = str(input())
    lts = lt.split(";")
    ltss = lts[0].split()
    ltse = lts[1].split()
    lt = int(ltss[0]) - (int(ltss[1]) / 60) - (float(ltss[2]) / 3600)
    lg = int(ltse[0]) - (int(ltse[1]) / 60) - (float(ltse[2]) / 3600)
    if -90 <= lt <= 90 and -180 <= lg <= 180:
        break
if lt < 0:
    print("Sul", end=" ")
else:
    if lt == 0:
        print("Equador", end=" ")
    else:
        print("Norte", end=" ")
if lg < 0:
    print("Oeste")
else:
    if lg == 0:
        print("Greenwich")
    else:
        print("Leste")
