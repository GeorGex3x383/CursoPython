import datetime

mi_hora = datetime.time(17,35)

print(type(mi_hora))
print(mi_hora)

mi_dia = datetime.date(2025,10,17)
print(mi_dia)

mi_fecha = datetime.datetime(2025,5,15,23,2,13,1700)
mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)
print(mi_fecha.today())

nacimiento = datetime.date(1999,5,25)
defuncion = datetime.date(2095,10,3)

vida = defuncion - nacimiento
print(vida)

minutos = datetime.datetime.now()
minutos2 = minutos.strftime('%M')
print(minutos)
print(minutos2)