import datetime
m = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
     "Novembro", "Dezembro"]
while True:
    d = str(input("Data: "))
    d = d.replace("/", " ")
    if 1 <= int(d.split()[0]) <= 31 \
            and 1 <= int(d.split()[1]) <= 12 \
            and 1900 <= int(d.split()[2]) <= int(datetime.date.today().strftime("%Y")):
        break
print(f"Você nasceu no dia {d.split()[0]} de {m[int(d.split()[1])]} de {d.split()[2]}. Correto? ")
