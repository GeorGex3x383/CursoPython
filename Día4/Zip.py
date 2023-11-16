nombres = ["Ana","Hugo","Valeria"]
edades = [65,29,15]
ciudades = ["Lima","Madrid","México"]

combinados = list(zip(nombres,edades,ciudades))

print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")