#Luego crea un script main.py en el mismo directorio en el que deberás importar el módulo y
#jecutar las funciones.


import modulo_numeros

def main():
    lista = modulo_numeros.generar_lista_aleatoria()
    
    print("Lista generada:")
    modulo_numeros.mostrar_lista(lista)
    
    lista_ordenada = modulo_numeros.ordenar_lista(lista)
    print("Lista ordenada:")
    modulo_numeros.mostrar_lista(lista_ordenada)

if __name__ == "__main__":
    main()
