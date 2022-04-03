while True:
    while True:
        q = int(input())
        if 0 <= q <= 30:
            break
    if q != 0:
        l = str(input()).split()
        s = v = 0
        if l[0] != "0":
            for i in range(len(l)):
                if 1 <= float(l[i]) <= 5000:
                    s += 1
                    v += float(l[i])
            if s == len(l) == q:
                print(f"{v/9.5 * 5.6:.2f}")
        else:
            break
    else:
        break
