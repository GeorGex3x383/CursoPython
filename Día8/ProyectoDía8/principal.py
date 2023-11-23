from numeros import *
from os import system

def limpiar_pantalla():
    system("cls")
    
def sacar_otro():
    x = True
    y = False
    while x == True:
        print("Desea sacar otro turno? S/N")
        turno = input("--> ")
        if turno not in ['S','s','N','n']:
            print("Turno no válido")
        else:
            if turno == 'S' or turno == 's':
                y = True
                x = False
            else:
                y = False
                x = False
    return y
        

def menu_opciones():
    limpiar_pantalla()
    opcion = ''
    while opcion != 4:
        print("Bienvenido! A que area se dirige?\n1. Perfumería.\n2. Farmacia.\n3. Cosmeticos.\n")
        opcion = input("--> ")
        limpiar_pantalla()
        match opcion:
                case '1':
                    decorar_ticket('p')
                    op = sacar_otro()
                    limpiar_pantalla()
                    if op == False:
                        break
                case '2':
                    decorar_ticket('f')
                    op = sacar_otro()
                    limpiar_pantalla()
                    if op == False:
                        break
                case '3':
                    decorar_ticket('c')
                    op = sacar_otro()
                    limpiar_pantalla()
                    if op == False:
                        break
                case _:
                    print("Opción inválida, intente de nuevo.")
    print("Gracias por venir")
    
menu_opciones()