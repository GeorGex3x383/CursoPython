from pathlib import Path

carpeta = Path("C:/Users/jemil/Documents/CursosYMas/PythonGratis")
archivo = carpeta / "otro_archivo.txt"

mi_archivo = open(archivo)
print(mi_archivo.read())
mi_archivo.close()