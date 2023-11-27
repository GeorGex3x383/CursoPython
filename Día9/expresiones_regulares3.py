import re

clave = input("clave: ")
patron = r'\D{1}\w{7}'

checar = re.search(patron,clave)
print(checar)