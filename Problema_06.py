"""""

Problema 6:
Una tienda de autopartes necesita un programa para catalogar sus productos, crear la clase
Catálogo y Producto, realizar un objeto dentro de un catálogo productos el cual debe tener un
método para agregar productos y otra para mostrar toda la lista de productos.
Agregar 2 funcionalidades al catálogo (por ejemplo, filtro según año) , asi mismo se puede
agregar más atributos a los productos para que se puedan hacer otras funcionalidades

"""""


class Producto:
    def __init__(self, nombre, precio, año, categoria):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        self.categoria = categoria

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: ${self.precio}, Año: {self.año}, Categoría: {self.categoria}"

class Catálogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        filtrados = [producto for producto in self.productos if producto.año == año]
        return filtrados

    def buscar_por_nombre(self, nombre):
        encontrados = [producto for producto in self.productos if nombre.lower() in producto.nombre.lower()]
        return encontrados

catalogo = Catálogo()

catalogo.agregar_producto(Producto("Filtro de aceite", 15.99, 2021, "Mantenimiento"))
catalogo.agregar_producto(Producto("Batería", 89.99, 2023, "Eléctrico"))
catalogo.agregar_producto(Producto("Neumático", 120.00, 2022, "Ruedas"))

print("Todos los productos:")
catalogo.mostrar_productos()

año = 2022
print(f"\nProductos del año {año}:")
productos_por_año = catalogo.filtrar_por_año(año)
for producto in productos_por_año:
    print(producto)

nombre = "batería"
print(f"\nBúsqueda de productos con nombre '{nombre}':")
productos_por_nombre = catalogo.buscar_por_nombre(nombre)
for producto in productos_por_nombre:
    print(producto)
