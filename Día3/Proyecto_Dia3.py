# Analizador de texto
texto = (input("Ingresa un texto: ")).lower()
a = (input("Agrega la primera letra: ")).lower()
b = (input("Agrega la segunda letra: ")).lower()
c = (input("Agrega la tercera letra: ")).lower()
texto_dividido = texto.split()
texto_invertido = " ".join(texto_dividido)

print(f"En el texto la letra {a} aparece {texto.count(a)} veces, la letra {b} aparece {texto.count(b)} veces y la letra {c} aparece {texto.count(c)} veces.\n")
print(f"El texto tiene {len(texto_dividido)} palabras.\n")
print(f"La primera letra del texto es {texto[0]} y la última es {texto[-1]}.\n")
texto_dividido.reverse()
texto_invertido = " ".join(texto_dividido)
print(f"Si el texto se invirtiera se vería así: {(texto_invertido)}.\n")
print(f"Aparece python? {"python" in texto}.\n")

# Código corrección para que funcione la busqueda de python.
buscar = "python" in texto
dic = {True:"sí", False:"no"}
print(f"Aparece python? {dic[buscar]}.\n")

""" Solución para ver si la palabra python se encuentra en el texto
print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")
"""