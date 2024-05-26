#Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás
#importar el módulo y ejecutar las funciones.

import operaciones

def main():
    # Ejemplos de operaciones
    print("Suma de 10 y 5:", operaciones.suma(10, 5))
    print("Resta de 10 y 5:", operaciones.resta(10, 5))
    print("Producto de 10 y 5:", operaciones.producto(10, 5))
    print("División de 10 por 5:", operaciones.division(10, 5))
    
    # Ejemplos con errores
    print("División de 10 por 0:", operaciones.division(10, 0))
    print("Suma de 10 y 'cinco':", operaciones.suma(10, 'cinco'))
    print("Producto de 'diez' y 5:", operaciones.producto('diez', 5))

if __name__ == "__main__":
    main()
