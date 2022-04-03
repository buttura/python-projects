from datetime import date
a = int(input("Digite o ano de nascimento: "))
if date.today().year - a <= 9:
    print("MIRIM")
elif date.today().year - a <= 14:
    print("INFANTIL")
elif date.today().year - a <= 19:
    print("JUNIOR")
elif date.today().year - a <= 20:
    print("SÊNIOR")
else:
    print("MASTER")
