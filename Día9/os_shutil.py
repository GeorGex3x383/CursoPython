import os 
import shutil
import send2trash

print(os.getcwd())

ruta = 'C:\\Users\\jemil\\Documents\\CursosYMas\\CursoPython'

for carpeta,subcarpeta,archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print("Las carpetas son:")
    for sub in subcarpeta:
        print(f"\t {sub}")
    print('Los archivos son:')
    for arch in archivo:
        print(f"\t {arch}")
    print("\n")