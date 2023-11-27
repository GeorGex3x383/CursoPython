import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

"""palabra = 'ayuda' in texto
print(palabra)"""

patron = 'ayuda'

busqueda = re.search(patron,texto)
busqueda2 = re.findall(patron,texto)

print(busqueda)
print(len(busqueda2))
