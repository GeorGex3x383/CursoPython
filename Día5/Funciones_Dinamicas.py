"""
def checar_tres_cifras(num):
    """
    #Función para ver si un numero tiene 3 cifras.
    #return: Bool true si cumple, false si no.
"""
    return num in range(100,1000)

resultado = checar_tres_cifras(657)
print(resultado)
"""

def checar_tres_cifras(lista):
    """
    Función para ver si un numero tiene 3 cifras.
    return: Bool true si cumple, false si no.
    """
    lista_3_cifras = []
    for num in lista:
        if num in range(100,1000):
            lista_3_cifras.append(num)
        else:
            pass
    return lista_3_cifras

resultado = checar_tres_cifras([555,99,600])
print(resultado)
