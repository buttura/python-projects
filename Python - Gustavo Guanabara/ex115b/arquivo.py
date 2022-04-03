from interface import *

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
    except:
        print("\033[1;31mHouve um erro na criação do arquivo!\033[m")
    else:
        print(f"Arquivo {nome} criado com sucesso.")
    finally:
        a.close()


def lerarquivo(nome):
    cabecalho("PESSOAS CADASTRADAS")
    try:
        a = open(nome, "rt")
    except:
        print("\033[1;31mERRO: Houve um problema ao ver as pessoas cadastradas\033[m")
    else:
        for linha in a:
             v = linha.split(";")
             v[1] = v[1].replace("\n", "")
             print(f"{v[0]:<30} {v[1]:>3} anos")
    finally:
        a.close()


def appendarquivo(arq, nome="Desconhecido", idade=0):
    try:
        a = open(arq, "at")
    except:
        print("\033[1;31mHouve um erro na abertura do arquivo!\033[m")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("\033[1;31mHouve um erro na hora de escrever os dados!\033[m")
        else:
            print(f"Novo registro de {nome} adicionado com sucesso!")
        finally:
            a.close()
