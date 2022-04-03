# Analisar se um número digitado pelo usúario é primo
n = int(input("Digite um número: "))
s = 0
for i in range(n, 0, -1):
    if n % i == 0:
        s += 1
print(f"O número {n}", end=" ")
if s > 2:
    print(f"NÃO é PRIMO")
else:
    print(f"é PRIMO")
#s = 0
# Números primos de 0 até 500
#for i in range(500):
#    for x in range(500, 0, -1):
#        if i % x == 0:
#            s += 1
#    if s == 2:
#        print(i)
#    s = 0

