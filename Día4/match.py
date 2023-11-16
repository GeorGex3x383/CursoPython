serie = 1
match serie:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case _:
        print("No existe")

cliente = {"nombre":"Jorge","edad":24,"ocupacion":"estudiante"}
pelicula = {"titulo":"matrix","ficha_tecnica":{"protagonista":"keanu reeves","director":"lana y lily"}}

elementos = [cliente,pelicula,"libro"]

for e in elementos:
    match e:
        case {"nombre":nombre,
              "edad":edad,
              "ocupacion":ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {"titulo":titulo,
              "ficha_tecnica": {"protagonista":protagonista,
                                "director":director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("no se que es")