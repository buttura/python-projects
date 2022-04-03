while True:
    while True:
        n = int(input())
        if n >= 0:
            break
    if n != 0:
        print(f"{n}! = ", end="")
        for i in range(n-1, 0, -1):
            if i == (n-1):
                print(n, end=" x ")
            if i != 0:
                n *= i
                print(i, end="")
            print(" x" if i > 1 else " =", end=" ")
        print(n)
    else:
        break
