monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas.")
    monedas -=1
else:
    print("No tengo más dinero.")

respuesta ="s"
while respuesta=="s":
    respuesta = input("Quieres seguir? s/n: ")
else:
    print("Gracias")

"""respuesta2 ="s"
while respuesta2=="s":
    pass    
    
print("Hola")"""

nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == "r":
        break
    print(letra)

nombre2 = input("Tu nombre: ")
for letra2 in nombre2:
    if letra2 == "r":
        continue
    print(letra2)