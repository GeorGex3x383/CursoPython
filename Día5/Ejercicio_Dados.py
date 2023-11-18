from random import randint

def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return (dado1,dado2)

def evaluar_jugada(dato1,dato2):
    suma_dados = dato1+dato2
    mensaje = ""
    if suma_dados <= 6:
        mensaje = f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        mensaje = f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        mensaje = f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    
    return mensaje

dado1,dado2 = lanzar_dados()
ver = evaluar_jugada(dado1,dado2)
print(ver)