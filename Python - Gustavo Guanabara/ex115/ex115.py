from ex115m import *
from time import sleep
from arquivo import *
from cadastro import *

arq = "cursoemvideo.txt"

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        cadastrarpessoa(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[1;31mERRO! Digite uma opçào válida!\033[m")
    sleep(1)
