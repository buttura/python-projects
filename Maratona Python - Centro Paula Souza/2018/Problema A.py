lista = list()
while True:
    n = str(input())
    lista.clear()
    #Adiciono os valores digitados em String
    lista.append(n.split())
    for i in range(0, len(lista[0])):
        if int(lista[0][i]) < 10:
            #Substituo os valores que são menores que 10, acrescentado um zero antes do número
            lista[0][i] = f"0{lista[0][i]}"
    if n != '0':
        if (1 <= int(lista[0][0]) <= 60) and (1 <= int(lista[0][1]) <= 60) and (1 <= int(lista[0][2]) <= 60) and (1 <= int(lista[0][3]) <= 60) and (1 <= int(lista[0][4]) <= 60) and (1 <= int(lista[0][5]) <= 60) and (len(lista[0]) == 6):
            break
    else:
        break
f = ""
#Crio um dicionario para armazenar a inicial da dezena e a quantidade que essa dezena aparece
dq = dict()
for i in range(0, len(lista[0])):
    # A string "f" vai receber todas as iniciais das dezenas
    f += lista[0][i][0]
    # O dicionario com o nome da inicial da dezena vai receber a quantidade de vezes que aparece aquela dezena
    dq[lista[0][i][0]] = f.count(lista[0][i][0])
# Dou um print para aparecer na tela a chave e o valor da chave no dicionário
for k, v in dq.items():
    print(f"{k} {v}", end=" ")
