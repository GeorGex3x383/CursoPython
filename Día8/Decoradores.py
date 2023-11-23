def decorar_saludo(funcion):
    
    def otra_funcion(texto):
        print("Hola")
        funcion(texto)
        print("Adios")
    return otra_funcion


def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayusculas)

mayusculas("fede")
mayuscula_decorada("fede")