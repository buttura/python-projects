from math import trunc
sbm = sbc = 0
while True:
    d = int(input())
    if 1 <= d <= 180:
        break
for i in range(0, d):
    while True:
        bm = int(input())
        sbm += bm
        bc = int(input())
        sbc += bc
        if 1 <= bm <= 1000 and 1 <= bc <= 1000:
            break
print(f"Milho verde: {trunc((sbm*200)/1000)}Kg")
print(f"Óleo vegetal: {trunc(((sbm*200) + (sbc*120))/1000)}L")
print(f"Açucar: {trunc(((sbm*250) + (sbc*360))/1000)}Kg")
print(f"Fubá: {trunc((sbm*200)/1000)}Kg")
print(f"Ovos: {trunc((sbm*4) + (sbc*4))}")
print(f"Farinha de Trigo: {trunc(((sbm*15) + (sbc*240))/1000)}Kg")
print(f"Coco ralado: {trunc(((sbm*15) + (sbc*100))/1000)}Kg")
print(f"Fermento em pó: {trunc(((sbm*5) + (sbc*10))/1000)}Kg")
print(f"Leite de Coco: {trunc((sbc*200)/1000)}L")
