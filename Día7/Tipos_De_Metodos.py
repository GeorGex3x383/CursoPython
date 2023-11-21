class Pajaro:

    alas = True

    def __init__(self,color, especie):
        self.color = color
        self.especie = especie

    def piar(self): #Método de instancia
        print("pío, mi color es {}".format(self.color))

    def volar(self,metros): #Método de instancia
        print(f"El pajaro ha volado {metros} metros.")
        self.piar()

    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es {self.color}")
    
    @classmethod #Método de clase no nesecitan una intsnacia para poder ejecutarse.
    def poner_huevos(cls, cantidad): #No puede acceder a self.
        print(f"Puso {cantidad} de huevos")
        cls.alas = False #Podemos acceder a los atributos de clase
        
    @staticmethod #Método estatico
    def mirar():
        print("El pajaro mira")

Pajaro.poner_huevos(6)
Pajaro.mirar()
#piolin.pintar_negro()
#piolin.volar(80)
#piolin.alas = False #Metodos de instancia modifican 
#print(piolin.alas)