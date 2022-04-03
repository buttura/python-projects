n = c = s = 0
while n != 999:
    n = int(input(f"[ {c + 1} ] Digite um valor: "))
    c += 1
    s += n
print(f"Foram digitados {c-1} números e a soma entre eles é {s-999}")