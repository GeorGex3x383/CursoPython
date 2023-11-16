from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorio2 = round(uniform(1,5),2)
print(aleatorio2)

aleatorio3 = random()
print(aleatorio3)

colores = ["rojo","verde","azul","amarillo"]
aleatorio4= choice(colores)
print(aleatorio4)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)