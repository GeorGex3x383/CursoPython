lista = ["a","b","c"]
for item in enumerate(lista):
    print(item)

for indice,item2 in enumerate(lista):
    print(indice,item2)

for indice3,item3 in enumerate(range(50,55)):
    print(indice3,item3)

mis_tuples = list(enumerate(lista))
print(mis_tuples)