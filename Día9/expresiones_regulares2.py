import re

texto = "Llama al 345-245-1234 ya mismo"

#patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron = r'\d{3}-\d{3}-\d{4}'

resultado = re.search(patron,texto)
print(resultado)