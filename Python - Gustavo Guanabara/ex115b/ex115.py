import interface
from time import sleep
from arquivo import *

arq = "cursoemvideo.txt"
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"])
    sleep(1)
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        interface.cabecalho("NOVO CADASTRO")
        nome = str(input("Digita o nome: "))
        idade = leiaint("Idade: ")
        appendarquivo(arq, nome, idade)
    elif resposta == 3:
        print("Saindo do programa...")
        break
    else:
        print("Digita um número válido!")
