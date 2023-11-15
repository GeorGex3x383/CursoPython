texto = "Este es el texto de Jorge"
resultado = texto.upper()
resultado1 = texto.lower()
resultado2 = texto.split()
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
resultado3 = " ".join([a,b,c,d]) #Se puede cambiar el espacio por cualquier caracter
resultado4 = texto.find("f") #Si no esta en el texto regresa un -1
resultado5 = texto.replace("Jorge","Eddy")
resultado6 = texto.replace("o","A")

print(resultado)
print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)