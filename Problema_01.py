"""""

Problema 1:
Implemente un programa que solicite al usuario una fracción, con
formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más
cercano, donde se indicará la cantidad de combustible en el
tanque. Se debe tener en cuenta los siguientes casos:
- Colocar E en caso X/Y sea menor a 1% del total
- Colocar F en caso X/Y sea mayor a 99%.
- En otro caso, devolver el valor en porcentaje %
También debe tomar en cuenta los siguientes casos:
- X y Y deben ser números enteros
- X debe ser menor o igual a Y, y Y != 0
De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
cualquier excepción como ValueError o ZeroDivisionError.

"""""


def obtener_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción (X/Y): ")
            x, y = fraccion.split("/")
            x = int(x)
            y = int(y)
            
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError("El numerador no puede ser mayor que el denominador.")
            
            return x, y
        except ValueError:
            print("Error: asegúrese de que ambos valores sean números enteros y que el numerador no sea mayor que el denominador.")
        except ZeroDivisionError:
            print("Error: el denominador no puede ser cero.")

def calcular_porcentaje(x, y):
    return (x / y) * 100

def mostrar_porcentaje():
    while True:
        x, y = obtener_fraccion()
        porcentaje = calcular_porcentaje(x, y)
        
        if porcentaje < 1:
            print("E")
        elif porcentaje > 99:
            print("F")
        else:
            print(f"{round(porcentaje)}%")

mostrar_porcentaje()
