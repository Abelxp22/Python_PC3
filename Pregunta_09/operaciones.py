"""""

Problema 9:
Cree un módulo llamado operaciones.py el cual contendrá 4 funciones para realizar una suma,
una resta, un producto y una división entre dos números. Todas ellas devolverán el resultado.
En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para
evitar que se quede bloqueada una funcionalidad, esto incluye:
● En caso de que se envíen valores a las funciones que no sean números, deberá
aparecer un mensaje que informe Error: Tipo de dato no válido.
● En caso de realizar una división por cero, deberá aparecer un mensaje que informe
Error: No es posible dividir entre cero.

"""""


def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido."

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido."

def producto(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido."

def division(a, b):
    try:
        if b == 0:
            return "Error: No es posible dividir entre cero."
        return a / b
    except TypeError:
        return "Error: Tipo de dato no válido."

if __name__ == "__main__":
    print(suma(10, 5))
    print(resta(10, 5))
    print(producto(10, 5))
    print(division(10, 0))
    print(division(10, "2"))
