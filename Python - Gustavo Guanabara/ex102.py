def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    for i in range(n, 0, -1):
        if show:
            print(f"{i}", end="")
            print(" x " if i != 1 else ' = ', end="")
        if i > 1:
            n *= (i-1)
    return n


print(fatorial(int(input("Digite um número: ")), False))
