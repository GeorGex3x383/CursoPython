class Animal:
    
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color
    
    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

piolin = Pajaro(34,"amarillo")

piolin.nacer()
print(piolin.color,piolin.edad)
#print(Pajaro.__bases__)
#print(Animal.__subclasses__())