"""archivo = open("prueba1.txt","w")

archivo.write("Soy el nuevo texto\n")
archivo.writelines(["Hola","Mundo","Aqui","Estoy"])

archivo.close()"""

"""archivo = open("prueba1.txt","w")

lista = ["Hola","Mundo","Aqui","Estoy"]

for p in lista:
    archivo.writelines(p + "\n")

archivo.close()"""

archivo = open("prueba.txt","a")

lista = ["Hola","Mundo","Aqui","Estoy"]

archivo.write("Bienvenido\n")

archivo.close()