"""""

Problema 5:
Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos
para:
1. Display - Debe mostrar toda la información del estudiante (nombre y número de
registro).
2. setAge - Debe asignar la edad al estudiante
3. setNota - Debe asignar las notas al estudiante.

"""""


class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = None

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas is not None:
            print(f"Notas: {self.notas}")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, notas):
        self.notas = notas

alumno = Alumno("Juan Pérez", "A12345")
alumno.display()

alumno.setAge(20)
alumno.setNota([85, 90, 78, 92])
alumno.display()


