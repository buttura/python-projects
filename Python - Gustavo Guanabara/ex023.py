#while True:
#    n = int(input("Digite um número: ")).
#    if 0 <= n <= 9999:
#        break
#print(f"Unidade: {n//1 % 10}\nDezena: {n//10 % 10}\nCentena: {n//100 % 10}\nMilhar: {n//1000 % 10}")
# OU
#while True:
#    n = str(input("Digite um número: ")).zfill(4)
#    if 0 <= int(n) <= 9999:
#        break
#print(f"Unidade: {n[3]}\nDezena: {n[2]}\nCentena: {n[1]}\nMilhar: {n[0]}")
# OU
while True:
    n = str(input("Digite um número: "))
    if 0 <= int(n) <= 9999:
        break
no = ""
for i in range(4 - len(n)):
    no += '0'
no += n
print(f"Unidade: {no[3]}\nDezena: {no[2]}\nCentena: {no[1]}\nMilhar: {no[0]}")
