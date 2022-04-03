from datetime import date
dtemp = dict()
l = list()
si = 0
while True:
    n = str(input("Nome: "))
    while True:
        s = str(input("Sexo: ")).strip()[0]
        if s in 'Ff' or s in 'Mm':
            break
    while True:
        a = int(input("Ano de nascimento: "))
        if 1900 <= a <= date.today().year:
            break
    si += date.today().year - a
    dtemp["Nome"] = n
    dtemp["Sexo"] = s
    dtemp["Idade"] = date.today().year - a
    l.append(dtemp.copy())
    print(l)
    dtemp.clear()
    r = str(input("Deseja continuar? ")).strip()[0]
    if r in 'Nn':
        break
print(f"- Foram cadastradas {len(l)} pessoas.\n- A média de idade do grupo: {si/len(l):.2f}")
print("- As mulheres cadastradas foram:", end=" ")
for i in range(len(l)):
    if l[i]['Sexo'] in "Ff":
        print(l[i]['Nome'], end=" ")
print("- Lista das pessoas que estão acima da média: ")
for i in range(len(l)):
    if l[i]["Idade"] > si/len(l):
        print(f"  -> {l[i]['Nome']} com {l[i]['Idade']} anos.")
