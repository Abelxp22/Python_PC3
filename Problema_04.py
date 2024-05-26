"""""

Problema 4:
Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
atributos de la clase.

"""""

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

rectangulo = RECTANGULO(8, 4) #---> Se puede dar la base y altura a elección

print(f"El área del rectángulo con largo {rectangulo.largo} y ancho {rectangulo.ancho} es {rectangulo.calcular_area()}")