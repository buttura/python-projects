n = str(input("Digite o nome completo: "))
print(f"O nome com todas as letras maiúsculas: {n.upper()}"
      f"\nO nome com todas as letras minúsculas: {n.lower()}"
      f"\nQuantidade de letras: {len(n.replace(' ', ''))}"
      f"\nQuantidade de letras apenas no primeiro nome: {len(n.split()[0])}")
