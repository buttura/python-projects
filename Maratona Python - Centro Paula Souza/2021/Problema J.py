num1a19 = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
num20a100 = ('vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa', 'cem')
num101a900 = ('cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos')

while True:
    num = float(input("Digite quanto você tem na sua carteira: [0 até 100000 reais] R$"))
    if 0 <= num <= 100000:
        break
m = (f"{num:.2f}")
c = m[-2:]

if num == 0:
    print('zero', end="")
else:
    if num < 20:
        print(num1a19[int(num)-1], end=" ")
        print("reais", end=" ")
    else:
        if num < 100:
            print(num20a100[int(str(num)[0])-2], end="")
            if int(str(num)[-1]) != 0:
                print(" e ", end="")
                print(num1a19[int(str(num)[-1])-1], end=" ")
            print("reais", end=" ")
        else:
            if num < 1000:
                if num == 100:
                    print(num20a100[-1], end=" ")
                else:
                    if num > 100:
                        print(num101a900[int(str(num)[0])-1], end="")
                        if int(str(num)[1]) != 0:
                            print(" e ", end="")
                            if int(str(num)[1]) == 1:
                                print(num1a19[int(str(num)[1:])-1], end="")
                            else:
                                print(num20a100[int(str(num)[1])-2], end="")
                        if int(str(num)[2]) != 0:
                            print(" e ", end="")
                            print(num1a19[int(str(num)[2])-1], end=" ")
                print("reais", end=" ")
            else:
                if num < 10000:
                    if num == 1000:
                        print(num1a19[0], end=" mil ")
                    else:
                        print(num1a19[int(str(num)[0])-1], end=" mil")
                        if int(str(num)[1]) != 0:
                            print(" e ", end="")
                            print(num101a900[int(str(num)[1])-1], end="")
                        if int(str(num)[2]) != 0:
                            print(" e ", end="")
                            print(num20a100[int(str(num)[2])-2], end="")
                        if int(str(num)[3]) != 0:
                            print(" e ", end="")
                            print(num1a19[int(str(num)[3])-1], end=" ")
                    print("reais", end=" ")
                else:
                    if num <= 100000:
                        if num == 100000:
                            print(num20a100[-1], end=" mil ")
                        else:
                            if int(str(num)[0]) == 1:
                                print(num1a19[int(str(num)[:2])-1], end=" mil")
                            else:
                                print(num20a100[int(str(num)[0])-2], end=" ")
                                if int(str(num)[1]) != 0:
                                    print("e ", end="")
                                    print(num1a19[int(str(num)[1])-1], end=" mil")
                                else:
                                    print("mil", end="")
                            if int(str(num)[2]) != 0:
                                print(" e ", end="")
                                print(num101a900[int(str(num)[2])-1], end="")
                            if int(str(num)[3]) != 0:
                                print(" e ", end="")
                                print(num20a100[int(str(num)[3])-2], end="")
                            if int(str(num)[4]) != 0:
                                print(" e ", end="")
                                print(num1a19[int(str(num)[4])-1], end=" ")
                    print("reais", end=" ")
if int(c) != 0:
    print("e ", end="")
    if int(c) != 0:
        if 0 < int(c) < 20:
            print(num1a19[int(c)-1], end="")
        else:
            print(num20a100[int(c[0])-2], end="")
            if int(c[1]) != 0:
                print(" e ", end="")
                print(num1a19[int(c[1])-1], end="")
    print(" centavos ")
