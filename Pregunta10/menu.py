# Creando el mennu en el ejercicio

import formas

def main():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = formas.CIRCULO(radio)
            print(f"El área del círculo es: {circulo.calcular_area():.2f}")
        
        elif opcion == "2":
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo = formas.RECTANGULO(largo, ancho)
            print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
        
        elif opcion == "3":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = formas.CUADRADO(lado)
            print(f"El área del cuadrado es: {cuadrado.calcular_area()}")
        
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()
