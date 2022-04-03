from datetime import date
s = 0
for i in range(0, 7):
    a = int(input(f"[ Pessoa {i+1} ] ano de nascimento: "))
    if date.today().year - a >= 18:
        s += 1
print(f"{s} atigiram a maioridade e {7 - s} ainda estão jovens.")
