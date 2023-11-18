def ceros_consecutivos(*args):
    lista = []
    cuenta = 0
    for arg in args:
        lista.append(arg)
    for num in lista:
        if cuenta >= len(lista):
            return False
        else: 
            if num == 0 and lista[cuenta+1] == 0:
                return True
            else:
                cuenta+=1
    return False

print(ceros_consecutivos(5,6,1,0,0,9,3,5))
print(ceros_consecutivos(6,0,5,1,0,3,0,1))
print(ceros_consecutivos(6,0,0,1,0,3,0,1))

# Solución de profesor
def ceros_vecinos(*args):
    contador=0
    for n in args:
        if contador+1 == len(args):
            return False
        elif args[contador] == 0 and args[contador+1] == 0:
            return True
        else: 
            contador+=1

    return False

print(ceros_vecinos(5,6,1,0,0,9,3,5))
print(ceros_vecinos(6,0,5,1,0,3,0,1))
print(ceros_vecinos(6,0,0,1,0,3,0,1))
print(ceros_vecinos(6,4,0,1,0,3,1,0))