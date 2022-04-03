from datetime import date
a = int(input("Digite o ano de nascimento: "))
if date.today().year - a < 18:
    print(f"Você vai se alistar ao serviço militar daqui {18 - date.today().year - a} anos.")
elif date.today().year - a == 18:
    print("Está na hora de se alistar ao serviço militar!")
else:
    print(f"Você já passou do tempo de alistamento ao serviço militar há {date.today().year - a - 18} anos.")
