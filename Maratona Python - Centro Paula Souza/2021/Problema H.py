while True:
    l = str(input()).split()
    if l[0] == "0":
        break
    else:
        if (float(l[0]) + float(l[1])) > float(l[2]) and (float(l[0]) + float(l[2])) > float(l[1]) and (float(l[1]) + float(l[2])) > float(l[0]):
            if float(l[0]) == float(l[1]) == float(l[2]):
                print("Triângulo equilátero!")
            elif float(l[0]) == float(l[1]) and float(l[0]) != float(l[2]) or float(l[0]) == float(l[2]) and float(l[0]) != float(l[1]) or float(l[1]) == float(l[2]) != float(l[0]):
                print("Triângulo isósceles!")
            else:
                print("Triângulo escaleno!")
        else:
            print("Os lados informados não formam um triângulo!")