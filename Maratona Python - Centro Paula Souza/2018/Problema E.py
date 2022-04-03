while True:
    s = str(input())
    s += " "
    if 3 <= len(s) <= 500:
        break
lista = list()
for i in range(0, len(s)):
    lista.append(s[i])
soma = 0
for k, v in enumerate(lista):
    if k + 1 < len(lista):
        if v != lista[k + 1]:
            if lista.count(v) == 3:
                soma += 10
            if lista.count(v) == 4:
                soma += 30
            if lista.count(v) == 5:
                soma += 50
print(soma)

