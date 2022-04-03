from ex115m import *


def arquivoexiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerarquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Houve um ERRO ao ver as pessoas cadastradas")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace('\n', '')
            print(f"{dado[0]:<30} {dado[1]:>3} anos")
    finally:
        a.close()
