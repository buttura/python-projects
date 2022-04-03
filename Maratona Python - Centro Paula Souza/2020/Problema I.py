while True:
    n = int(input())
    if 1 <= n <= 50000:
        break
f = ""
for i in range(len(str(bin(n)[2:]))-1, -1, -1):
    f += str(bin(n)[2:])[i]
if str(bin(n)[2:]) == f:
    print("V")
else:
    print("F")
