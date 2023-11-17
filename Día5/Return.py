def multiplicar(num1,num2):
    """
    Esta función multiplica dos numeros.
    return: regresa el resultado de la multiplicación.
    """
    total = num1*num2
    return total
resultado = multiplicar(5,5)
print(resultado)

def invertir_palabra(palabra):
    """
    Esta función recibe una palabra y la invierte.
    return: palabra invertida
    """
    resultado = palabra.upper()
    resultado = list(resultado)
    resultado.reverse()
    return "".join(resultado)
palabra = "Python"

resultado = invertir_palabra(palabra)
print(resultado)
