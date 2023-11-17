precios_de_cafe = [("capuccion",1.50),("expresso",2.5),("mocha",1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_caro = ""

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
        else:
            pass

    return (cafe_caro,precio_mayor)

cafe,precio = cafe_mas_caro(precios_de_cafe)
print(f"El cafe más caro es {cafe} con un costo de ${precio}.")