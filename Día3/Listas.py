mi_lista = ["a","b","c"]
otra_lista = ["Hola",55,30.33]

otra_lista[0] = "Mundo"

print(type(mi_lista))
print(type(otra_lista))
print(len(mi_lista))
print(mi_lista[0:2])
print(mi_lista+otra_lista)

mi_lista.append("d")
print(mi_lista)
mi_lista.pop(2)
print(mi_lista)

mi_lista2 = ["f", "k", "x", "s", "a"]
mi_lista2.sort()
print(mi_lista2)
mi_lista2.reverse()
print(mi_lista2)