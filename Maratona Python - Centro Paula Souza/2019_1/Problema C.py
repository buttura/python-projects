veiculos = []
veiculo = []
k = c = 0
while True:
    qntdv = int(input("Quantidade de veículos: "))
    if 1 <= qntdv <= 100:
        break
for i in range(0, qntdv):
    while True:
        v = str(input("Placa: ")).strip()
        if v not in veiculo:
            veiculo.append(v)
            break
    while True:
        km = int(input("Km rodados: "))
        if 1 <= km <= 2000:
            veiculo.append(km)
            break
    while True:
        li = int(input("Litros gastos: "))
        if 1 <= li <= 800:
            veiculo.append(li)
            break
    veiculos.append(veiculo[:])
    veiculo.clear()
for i in range(0, len(veiculos)):
    k += veiculos[i][1]
    c += veiculos[i][2]
m = k/c
for x in range(0, len(veiculos)):
    if (veiculos[x][1] / veiculos[x][2]) < m:
        print(veiculos[x][0])

