vfnaj = ['V', 'F', 'A', 'N', 'J']
# Primeiro fiz uma lista "decrescente" de acordo com os valores que cada letra propõe ao exercício
lista = []
while True:
    q = int(input())
    #Quantidade de testes
    if 1 <= q <= 50:
        break
for i in range(0, q):
    while True:
        n = int(input())
        # Quantidade de dispositivos
        if 1 <= n <= 10000:
            break
    for x in range(0, n):
        while True:
            # Dispositivo
            d = str(input())
            # Se a última letra da string estiver na lista
            if d[-1].upper() in vfnaj:
                break
        # A lista não tem nenhuma entrada, apenas está vazia
        for c, v in enumerate(lista):
            # Se a última letra da string for igual "A", vai localizar o index na lista em que contém as letras
            # E se o index for == 2 ("A")
            if vfnaj.index(d[-1].upper()) == 2:
                # No enunciado é dito que se for A, anda 2 casas na lista. Portanto, vou usar um insert naquela posição
                # Posição - 3 e armazena o valor da string
                lista.insert(c-3, d)
                break
                # No enunciado é dito que se for F, anda 3 casas na lista. Portanto, vou usar um insert naquela posição
                # Posição - 4 e armazena o valor da string
            if vfnaj.index(d[-1].upper()) == 1:
                lista.insert(c-4, d)
                break
                # No entanto, se a última letra da string, vai localizar o index na lista em que contém as letras for me
                # nor que o último valor digitado, com o index na lista. Exemplo d[-1] == "F" e v[-1] == "J"
                #                                                                 index = 1      index = 4
            if vfnaj.index(d[-1].upper()) < vfnaj.index(v[-1].upper()):
                # No exemplo. Vai dar um insert na posição em que está armazenado o index = 4 e o valor da string
                lista.insert(c, d)
                break
        else:
            #Senão for nenhuma das opções, apenas da um append
            lista.append(d)
# Vai printar o que está na lista
for i in range(0, len(lista)):
    print(lista[i])
