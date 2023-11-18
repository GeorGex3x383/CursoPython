def devolver_distintos(num1,num2,num3):
    suma=num1+num2+num3
    lista = [num1,num2,num3]
    lista.sort()
    num_min = lista[0]
    num_med = lista[1]
    num_max = lista[2]

    if suma > 15:
        return num_max
    elif suma < 10:
        return num_min
    else:
        return num_med



res = devolver_distintos(3,4,7)
print(res)