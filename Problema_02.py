"""""

Problema 2:
Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad)

"""""


def obtener_calificaciones():
    calificaciones_input = input("Introduce una lista de calificaciones separadas por comas: ")

    calificaciones_str = calificaciones_input.split(',')

    calificaciones = []

    for calificacion_str in calificaciones_str:

        calificacion_str = calificacion_str.strip()

        try:
            calificacion = int(calificacion_str)
            calificaciones.append(calificacion)
        except ValueError:
            print(f"Error: '{calificacion_str}' no es una calificación válida.")

    return calificaciones

calificaciones_validas = obtener_calificaciones()
print("Calificaciones válidas:", calificaciones_validas)