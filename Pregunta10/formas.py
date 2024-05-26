"""""

Problema 10
Cree un menú que reutilice a manera de módulos las clases creadas en los ejercicios 3 y 4. El
menú para utilizar deberá tener las siguientes funcionalidades:
1. Calcular el área de un circulo
2. Calcular el área de un rectangulo
3. Calcular el área de un cuadrado
4. Salir.

"""""


import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

if __name__ == "__main__":
    circulo = CIRCULO(3)
    print(f"Área del círculo: {circulo.calcular_area():.2f}")
    
    rectangulo = RECTANGULO(15, 4)
    print(f"Área del rectángulo: {rectangulo.calcular_area()}")
    
    cuadrado = CUADRADO(6)
    print(f"Área del cuadrado: {cuadrado.calcular_area()}")
