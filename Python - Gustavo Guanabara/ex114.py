import urllib.request

dominio = str(input("Insira o site: "))

try:
    site = urllib.request.urlopen(f"http://www.{dominio}.com.br/")
except urllib.error.URLError:
    print(f"\033[1;31mO site {dominio.capitalize()} não está acessível no momento.\033[m")
else:
    print(f"\033[1;32mO site {dominio.capitalize()} está acessível no momento\033[m")
    print(site.read())
