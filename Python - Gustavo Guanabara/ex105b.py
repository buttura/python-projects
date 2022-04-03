def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    d = dict()
    d["Total"] = len(n)
    s = 0
    for i in range(len(n)):
        s += n[i]
        if i == 0:
            d["Maior"] = d["Menor"] = n[i]
        else:
            if n[i] > d["Maior"]:
                d["Maior"] = n[i]
            if n[i] < d["Menor"]:
                d["Menor"] = n[i]
    d["Media"] = s/len(n)
    if sit:
        if d["Media"] >= 7:
            d["Situacao"] = "BOA"
        elif d["Média"] >= 5:
            d["Situacao"] = "RAZOÁVEL"
        else:
            d["Situacao"] = "RUIM"
    return d


r = notas(5.5, 10, 9, 8.5, 2.5, sit=True)
print(r)
