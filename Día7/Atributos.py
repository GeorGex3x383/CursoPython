class Pajaro:

    alas = True

    def __init__(self,color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro("rojo","Tucan")

print(f"Mi pajaro es un {mi_pajaro.especie} color {mi_pajaro.color} y {mi_pajaro.alas}")

print(Pajaro.alas)