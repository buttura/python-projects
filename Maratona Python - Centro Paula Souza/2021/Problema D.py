while True:
    while True:
        m = str(input()).split("|")
        if 0 <= int(m[0]) <= 100000:
            break
    v = ((int(m[2].split(":")[0]) * 60 + int(m[2].split(":")[1])) - (int(m[1].split(":")[0]) * 60 + int(m[1].split(":")[1])))/60 * 2.30
    if m[0] == "0":
        break
    else:
        print(f"{m[0]}|{v:.2f}")
