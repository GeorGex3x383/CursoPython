# Juego contra la computadora en el que hay que adivinar un número entre 1 a 100 con 8 intnetos
from random import randint

nombre = input("Introduce tu nombre: ")
numero_secreto = randint(1,100)
intentos = 0
ganador = False

while (intentos != 8) and (ganador==False):
    numero_jugador = int(input(f"{nombre} he pensado un número del 1 al 100, introduce el número que creas que pense: "))
    if(numero_jugador>100 or numero_jugador<1):
        print("El numero no es valido, introduzca uno dentro del rango.")
    elif numero_jugador < numero_secreto:
        print("Tu numero es menor al numero que pense intenta de nuevo.")
        intentos+=1
        print(f"Te quedan {8-intentos} intentos.")
    elif numero_jugador > numero_secreto:
        print("Tu numero es mayor al numero que pense intenta de nuevo.")
        intentos+=1
        print(f"Te quedan {8-intentos} intentos.")
    elif numero_jugador == numero_secreto:
        print(f"Felicidades {nombre}, {numero_secreto} era el numero que pense y lo adivinaste en {intentos} intentos.")
        ganador = True
if(intentos == 8):
    print(f"Lo siento, perdiste. El numero que pense era: {numero_secreto}")

