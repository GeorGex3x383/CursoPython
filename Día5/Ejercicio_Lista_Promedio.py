def reducir_lista(lista):
    lista_unica = list(set(lista))
    lista_unica.remove(max(lista_unica))
    return lista_unica
    
def promedio(lista):
    suma = 0
    cuenta = 0
    for num in lista:
        suma+=num
        cuenta+=1
    return suma/cuenta

nueva_lista = []
lista_numeros = [1,2,15,7,2]
nueva_lista = reducir_lista(lista_numeros)
print(nueva_lista)
resultado = promedio(nueva_lista)
print(resultado)