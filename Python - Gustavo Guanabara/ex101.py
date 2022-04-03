def voto(a):
    from datetime import date
    print(f"Com {date.today().year - a} anos:", end=" ")
    if 18 <= date.today().year - a < 65:
        print("VOTO OBRIGATÓRIO.")
    elif date.today().year - a < 16:
        print("VOTO NEGADO.")
    else:
        print("VOTO OPCIONAL.")


voto(int(input("Em que ano você nasceu? ")))
