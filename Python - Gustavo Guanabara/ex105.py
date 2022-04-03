def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação do aluno.
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
    d["Média"] = s/len(n)
    if sit:
        if d["Média"] >= 7:
            d["Situação"] = "BOM"
        else:
            if d["Média"] >= 5:
                d["Situação"] = "RAZOAVEL"
            else:
                d["Situação"] = "RUIM"
    return d


r = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(r)
