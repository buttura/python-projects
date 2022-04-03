def leiadinheiro(f):
    l = list()
    while True:
        s = 0
        v = str(input(f)).strip().replace(",", ".")
        for i in range(len(v)):
            if v[i].isnumeric() or v[i] == ".":
                s += 1
        if (v.isalpha() or v == "") or (s != len(v)):
            print(f"""\033[1;31m[ERRO]: "{v}" é um preço inválido! \033[m""")
        else:
            break
    return float(v)
