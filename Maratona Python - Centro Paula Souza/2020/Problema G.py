s = 0
l = list()
while True:
    n = str(input())
    for i in range(0, len(n.split())):
        if 0 <= int(n.split()[i]) <= 20:
            s += 1
    if len(n.split()) == 8 and len(n.split()) == s:
        break
    else:
        s = 0

def mf(d1, d2, d3, a11, a12, a21, a22, a23):
    return d1 + d2 + d3 + (a11 + a12)/2 + (a21 + a22 + a23)/3


f = "aprovado"
nf = int(mf(int(n.split()[0]), int(n.split()[1]), int(n.split()[2]), int(n.split()[3]), int(n.split()[4]), int(n.split()[5]), int(n.split()[6]), int(n.split()[7])))
if 0 <= nf < 60:
    f = "reprovado"
else:
    if nf > 100:
        nf = 100
print(f"Aluno {f} com nota: {nf}")

