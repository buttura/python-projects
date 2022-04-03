n = str(input("Digite uma expressão: "))
if n.count("(") == n.count(")"):
    print("Expressão válida.")
else:
    print("Expressão inválida.")