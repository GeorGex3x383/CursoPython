import os 

ruta = os.getcwd()
ruta2 = os.chdir("C:\\Users\\jemil\\Documents\\CursosYMas\\PythonGratis")
#ruta3 = os.makedirs("C:\\Users\\jemil\\Documents\\CursosYMas\\PythonGratis\\Otra")
ruta4 = "C:\\Users\\jemil\\Documents\\CursosYMas\\CursoPython\\Día6\\prueba.txt"

os.rmdir("C:\\Users\\jemil\\Documents\\CursosYMas\\PythonGratis\\Otra")

elemento = os.path.basename(ruta4)
elemento2 = os.path.dirname(ruta4)
elemento3 = os.path.split(ruta4)
print(elemento)
print(elemento2)
print(elemento3)



"""archivo = open("otro_archivo.txt")

print(archivo.read())

archivo.close()"""