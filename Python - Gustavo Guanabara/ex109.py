import ex109m

n = ex109m.leiafloat("Digite o preço: R$")
print(f"A metade de {ex109m.moeda(n)} é {ex109m.metade(n, False)}")
print(f"O dobro de {ex109m.moeda(n)} é {ex109m.dobro(n, True)}")
print(f"Aumentando 10%, temos {ex109m.moeda(n)} é {ex109m.aumentar(n, 10, True)}")
print(f"Reduzindo 13%, temos {ex109m.moeda(n)}, é {ex109m.diminuir(n, 13, False)}")
