n = int(input("Digite um número: "))
print("[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal")
op = int(input("Sua opção: "))

if 1 <= op <= 3:
    print(f"A conversão do número {n}", end=" ")
    if op == 1:
        print(f"para binário: {bin(n)[2:]}")
    elif op == 2:
        print(f"para octal: {oct(n)[2:]}")
    elif op == 3:
        print(f"para hexadecimal: {hex(n)[2:]}")
else:
    print("Número inválido!")
