from time import sleep


def lin():
    print("--="* 10)


def maior(*num):
    lin()
    print("Analisando os valores passados...")
    m = 0
    for i in range(len(num)):
        print(num[i], end=" ")
        sleep(0.3)
        if i == 0:
            m = num[i]
        else:
            if num[i] > m:
                m = num[i]
    print(f"Foram informados {len(num)} valores ao todo.\nO maior valor informado foi {m}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
