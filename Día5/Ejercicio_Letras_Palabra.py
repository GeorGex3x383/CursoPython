def letras_palabras(palabra):
    resultado = list(palabra)
    resultado = list(set(palabra))
    resultado.sort()
    return resultado

res = letras_palabras("entretenido")
print(res)