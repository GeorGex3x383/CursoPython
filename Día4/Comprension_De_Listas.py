# Manera con muchas lineas
"""palabra = "python"
lista = []
for letra in palabra:
    lista.append(letra)

print(lista)"""

palabra = "python"
lista = [letra for letra in palabra]
print(lista)

numeros = [num for num in range(0,21,2) if num*2>10]
print(numeros)

numeros2 = [num if num*2>10 else 'no' for num in range(0,21,2)]
print(numeros2)

pies = [10,20, 30, 40, 50]
metros = [round(pie/3.281,2) for pie in pies]
print(metros)