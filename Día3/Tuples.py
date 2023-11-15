mi_tuple = (1,2,3,4)
mi_tuple2 = (1,3.4,"Hola")
print(type(mi_tuple))
print(mi_tuple[0])

mi_tuple3 = (1,2,(10,20),3)
print(mi_tuple3[2])
print(mi_tuple3[2][0])

mi_tuple3 = list(mi_tuple3)
print(type(mi_tuple3))

t = (1,2,3)
x,y,z = t
print(x,y,z)

t1 = (1,2,3,1)
print(len(t1))
print(t1.count(1))