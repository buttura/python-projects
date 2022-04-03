import datetime
ano = int(input("Digite um ano: "))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0:
    print(f"O ano {ano} é BISSEXTO!")
else:
    print(f"O ano {ano} NÃO é BISSEXTO!")
