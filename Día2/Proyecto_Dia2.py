"""
Proyecto para calcular las comisiones de un trabajador, se pedira el nombre y las comisiones 
y de resultado se entregara cuanto ganaron con respecto al 13%.
"""
nombre_empleado = input("Dame tu nombre: ")
ventas = input("Pon cuanto ganaste en ventas: ")
ventas = float(ventas)
comision = round((ventas*13)/(100),2)
print(f"Felicidades {nombre_empleado} las ganancias de tu esfuerzo son: ${comision} ¡Enhorabuena!")