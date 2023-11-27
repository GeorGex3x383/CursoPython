import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()
ruta = 'C:\\Users\\jemil\\Documents\\CursosYMas\\CursoPython\\Día9\\Mi_Gran_Directorio'
patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
numeros_encontrados = []
archivos_encontrados = []

def buscar_numero(archivo, patron):
    este_archivo = open(archivo,'r')
    texto = este_archivo.read()
    if re.search(patron,texto):
        return re.search(patron,texto)
    else:
        return ''
    
def crear_listas():
    for carpeta,subcarpetas,archivos in os.walk(ruta):
        for a in archivos:
            resultado = buscar_numero(Path(carpeta, a),patron)
            if resultado != '':
                numeros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())
                
def mostar_pantalla():
    contador = 0
    print('-'*40)
    print(f"Fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}")
    print("\n")
    print("ARCHIVO\t\t\tNo. serie")
    print("-------\t\t\t---------")
    for a in archivos_encontrados:
        print(f"{a}\t{numeros_encontrados[contador]}")
        contador+=1
    print("\n")
    print(f"Numeros encontrados: {len(numeros_encontrados)}")
    fin = time.time()
    duracion = fin-inicio
    print(f"Duración de busqueda: {math.ceil(duracion)} segundos")
    print('-'*40)
    
#Codigo
crear_listas()
os.system('cls')
mostar_pantalla()
    