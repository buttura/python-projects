v = ("A", "E", "I", "O", "U")
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for i in range(len(palavras)):
    print(f"Na palavra {palavras[i].upper()} temos: ", end="")
    for x in range(len(palavras[i])):
        if palavras[i][x].upper() in v:
            print(palavras[i][x], end=" ")
        if x == len(palavras[i])-1:
            print("\n")