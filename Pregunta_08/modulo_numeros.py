"""""

Problema 8:
Desarrollar un módulo que contenga las siguientes funciones:
● Que genere 20 números enteros aleatorios entre 0 y 100 y devuelva una lista.
● Mostrar la lista obtenida por pantalla.
● Ordenar los valores de la lista y mostrarla por pantalla.

"""""


import random

def generar_lista_aleatoria():
    """Genera una lista de 20 números enteros aleatorios entre 0 y 100."""
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    """Muestra la lista proporcionada por pantalla."""
    print(lista)

def ordenar_lista(lista):
    """Ordena la lista proporcionada y la devuelve."""
    return sorted(lista)

if __name__ == "__main__":
    lista = generar_lista_aleatoria()
    print("Lista generada:")
    mostrar_lista(lista)
    lista_ordenada = ordenar_lista(lista)
    print("Lista ordenada:")
    mostrar_lista(lista_ordenada)
