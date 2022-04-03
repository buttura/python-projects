import ex108m

n = ex108m.leiafloat("Digite um número: ")
print(f"A metade de {ex108m.moeda(n)} é {ex108m.moeda(ex108m.metade(n))}")
print(f"O dobro de {ex108m.moeda(n)} é {ex108m.moeda(ex108m.dobro(n))}")
print(f"Aumentando 10%, temos {ex108m.moeda(ex108m.aumentar(n, 10))}")
print(f"Reduzindo 10%, temos {ex108m.moeda(ex108m.diminuir(n, 10))}")
