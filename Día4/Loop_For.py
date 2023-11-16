lista = ["a","b","c","d"]
for letra in lista:
    num_letra = lista.index(letra)+1
    print(f"Letra {num_letra} es {letra}")

lista2 = ["Pablo","Laura","Luis", "Jorge", "Julia"]
for nombre in lista2:
    if nombre.startswith("L"):
        print(nombre)
    else:
        print("Nombre que no empieza con L")

numeros = [1,2,3,4,5]
mi_valor = 0

for num in numeros:
    mi_valor = mi_valor + num
    print(mi_valor)

print(mi_valor)

palabra = "python"
for letra in palabra:
    print(letra)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic = {1:"a",2:"b",3:"c"}
for item in dic.items():
    print(item)