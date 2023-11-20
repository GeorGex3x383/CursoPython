from pathlib import Path, PureWindowsPath
from os import system,listdir,makedirs,rmdir
base = Path.home()
ruta = Path(base,"Recetas")

def limpiar_pantalla():
    system("cls")

def bienvenida(ruta):
    cuenta = 0
    for txt in ruta.glob("**/*.txt"):
        cuenta+=1
    limpiar_pantalla()
    print(f"¡Bienvenido! Esta es tu ruta: {ruta}\nTienes {cuenta} recetas.")

def imprimir_menu_opciones(op):
    check = False
    while check == False:
        print("""Elige una opción: 
            1. Leer receta
            2. Crear recerta
            3. Crear categoría
            4. Eliminar receta
            5. Eliminar categoría
            6. Finalizar Programa""")
        op = input("--> ")
        if op not in ["1","2","3","4","5","6"]:
            limpiar_pantalla()
            print("Opción inválida.\n")
            check = False
        else:
            check = True
    return op

def mostar_categorias(ruta):
    num = 0
    categorias=listdir(ruta)
    print("Categorías: \n")
    for c in categorias:
        num+=1
        print(f"{num}. "+c)
    return categorias

def mostrar_recetas(ruta):
    num = 0
    recetas=listdir(ruta)
    print("Recetas: \n")
    for r in recetas:
        num+=1
        print(f"{num}. "+r)
    return recetas

def abrir_archivo_lectura(ruta):
    archivo = open(ruta)
    todas = archivo.readlines()
    print("\n")
    print(todas)
    archivo.close()

def crear_archivo(ruta):
    nombre = input("¿Qué nombre llevará esta receta? ")
    nombre = nombre+".txt"
    nueva_ruta = Path(ruta,nombre)
    texto = input("Aquí escribe el contenido de la receta: ")
    archivo = open(nueva_ruta,"w")
    archivo.write(texto)
    archivo.close()

#Programa
opcion = ''
categorias = []
recetas = []
bienvenida(ruta)
while opcion != "6":
    print("\n")
    opcion=imprimir_menu_opciones(opcion)
    limpiar_pantalla()
    match opcion:
        case "1":
            categorias=mostar_categorias(ruta)
            ele_cat = int(input("¿Que categoría eliges? "))
            nueva_ruta = Path(ruta,categorias[ele_cat-1])
            limpiar_pantalla()
            recetas=mostrar_recetas(nueva_ruta)
            ele_cat = int(input("¿Que receta eliges? "))
            nueva_ruta_r = Path(nueva_ruta,recetas[ele_cat-1])
            limpiar_pantalla()
            abrir_archivo_lectura(nueva_ruta_r)
        case "2":
            categorias=mostar_categorias(ruta)
            ele_cat = int(input("¿Que categoría eliges? "))
            nueva_ruta = Path(ruta,categorias[ele_cat-1])
            crear_archivo(nueva_ruta)
        case "3":
            nombre_cat = input("¿Cuál es el nombre de la nueva categoría? ")
            nueva_ruta = Path(ruta,nombre_cat)
            makedirs(nueva_ruta)
            print(f"Se creo la categoría {nombre_cat} exitosamente")
        case "4":
            categorias=mostar_categorias(ruta)
            ele_cat = int(input("¿Que categoría eliges? "))
            nueva_ruta = Path(ruta,categorias[ele_cat-1])
            limpiar_pantalla()
            recetas=mostrar_recetas(nueva_ruta)
            ele_cat = int(input("¿Que receta eliges? "))
            nueva_ruta_r = Path(nueva_ruta,recetas[ele_cat-1])
            limpiar_pantalla()
            ruta_windows = PureWindowsPath(nueva_ruta_r)
            print(f"Se ha borrado el archivo: {nueva_ruta_r.stem}")
            Path(ruta_windows).unlink()
        case "5":
            categorias=mostar_categorias(ruta)
            ele_cat = int(input("¿Que categoría eliges? "))
            nueva_ruta = Path(ruta,categorias[ele_cat-1])
            limpiar_pantalla()
            ruta_windows = PureWindowsPath(nueva_ruta)
            print(f"Se borro la categoria: {categorias[ele_cat-1]}")
            rmdir(ruta_windows)
        case "6":
            break

print("¡Hasta luego!")