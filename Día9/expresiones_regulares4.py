import re

texto = "No atendemos los lunes por la tarde"

buscar = re.findall(r'[^\s]+',texto)

print(buscar)