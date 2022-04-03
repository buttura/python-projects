p = float(input("Preço do produto: R$"))
print("[ 1 ] À vista dinheiro/cheque: 10% de desconto\n"
      "[ 2 ] À vista no cartão: 5% de desconto\n"
      "[ 3 ] Em até 2x no cartão: preço normal\n"
      "[ 4 ] 3x ou mais no cartão: 20% de juros")
op = int(input("Sua opção: "))
if 1 <= op <= 4:
    if op == 1:
        print(f"Com 10% de desconto no dinheiro/cheque, o produto custará R${p - p*10/100:.2f}")
    if op == 2:
        print(f"Com 5% de desconto no cartão, o produto custará R${p - p*15/100:.2f}")
    if op == 3:
        print(f"Em até 2x no cartão, o produto custará R${p:.2f}")
    if op == 4:
        print(f"Em 3x ou mais no cartão, o produto custará R${p + p*20/100:.2f}")
