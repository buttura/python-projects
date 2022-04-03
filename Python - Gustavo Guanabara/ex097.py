def msg(txt):
    print("-" * (len(txt)+4))
    print(f"{txt:^{len(txt)+4}}")
    print("-" * (len(txt)+4))


msg(str(input("Digite uma mensagem: ")))