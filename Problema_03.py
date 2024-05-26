"""""

Problema 3:
Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.

"""""

import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

circulo = CIRCULO(4)   #---> Se puede dar el radio a elección

print(f"El área del círculo con radio {circulo.radio} es {circulo.calcular_area():.2f}")
