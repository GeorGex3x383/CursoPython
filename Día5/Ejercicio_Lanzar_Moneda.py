from random import choice

def lanzar_moneda():
    moneda = choice(["Cara","Cruz"])
    return moneda

def probar_suerte(resultado,lista):
    if resultado == "Cara":
        print("La lista se autodestruirá")
        lista = []
        return lista
    else:
        print("La lista fue salvada")
        return lista


lista_numeros = [1,2,3,4,5]
res = lanzar_moneda()
nueva_lista = probar_suerte(res,lista_numeros)
print(nueva_lista)