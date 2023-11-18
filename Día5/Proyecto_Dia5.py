# Juego del ahorcado
from random import choice

def pedir_letra():
    letra = input("Ingresa una letra: ")
    return letra

def validar_letra(letra):
    if isinstance(letra, str) and len(letra) <=1 and letra.isalpha():
        return True
    else:
        return False
    
def checar_letra(spalabra,letra):
    if letra in spalabra:
        return True
    else:
        return False
    
def ver_si_gano(palabra):
    cuenta = False
    if "_" in palabra:
        return cuenta
    else:
        cuenta = True
        return cuenta

palabra_secreta = choice(["gato","motor","lalaland","jorge","arroz"])
lista_secreta = []
lista_letras_incorrectas = []
vidas = 6
for letra in palabra_secreta:
    lista_secreta.append("_")
palabra_secreta_muestra = "".join(lista_secreta)

print(palabra_secreta)
print(f"Bienvenido, he pensado en una palabra secreta, intentala adivinar! Tienes {vidas} vidas")
print(f"La palabra secreta de este juego se ve así: {palabra_secreta_muestra}")

while vidas > 0:
    letra = pedir_letra()
    validar = validar_letra(letra)
    if validar == True:
        checar = checar_letra(palabra_secreta,letra)
        if checar == True:
            print(f"Excelente la {letra} si estaba en la palabra secreta.")
            cuenta = 0
            for l in palabra_secreta:
                if l == letra:
                    lista_secreta[cuenta] = letra
                    cuenta+=1
                else:
                    cuenta+=1
        else:
            lista_letras_incorrectas.append(letra)
            print(f"Lo siento la {letra} no se encuentra en la palabra secreta.")
            vidas-=1

        palabra_secreta_muestra = "".join(lista_secreta)

        print(f"Estas son las letras incorrectas que has usado: {lista_letras_incorrectas}")
        print(f"{palabra_secreta_muestra}\t vidas: {vidas}")
        gano = ver_si_gano(palabra_secreta_muestra)
        if gano == True:
            print(f"Felicidades ganaste, y te quedaron: {vidas} vidas.")
            break
    else:
        print("El caracter que ingresaste no es válido, intenta de nuevo.")

if ver_si_gano(palabra_secreta_muestra) == False:
    print(f"Lo siento, te quedaste sin vidas :( La palabra secreta era: {palabra_secreta}")




