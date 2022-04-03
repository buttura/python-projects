def romano_para_inteiro(romano):
    romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    inteiro = 0

    for i in range(len(romano)):
        if i > 0 and romanos[romano[i]] > romanos[romano[i - 1]]:
            inteiro += romanos[romano[i]] - 2 * romanos[romano[i - 1]]
        else:
            inteiro += romanos[romano[i]]
    return inteiro


print(romano_para_inteiro("XLIX"))