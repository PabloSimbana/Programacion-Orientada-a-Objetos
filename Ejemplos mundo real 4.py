# Clase Producto: producto de la tienda
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Clase Tienda: maneja los productos y las ventas
class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Agrega un producto a la lista
        self.productos.append(producto)

    def mostrar_productos(self):
        # Muestra todos los productos disponibles
        print("Productos disponibles:")
        for p in self.productos:
            print(f"- {p.nombre}: ${p.precio}")

    def vender(self, nombre_producto):
        # Busca el producto por nombre y lo vende
        for p in self.productos:
            if p.nombre == nombre_producto:
                print(f"Producto vendido: {p.nombre} por ${p.precio}")
                return
        print("Producto no encontrado")

# ---------------- USO DEL PROGRAMA ----------------

# Crear tienda
tienda = Tienda()

# Crear productos
p1 = Producto("JUGO", 50)
p2 = Producto("Leche", 800)

# Agregar productos a la tienda
tienda.agregar_producto(p1)
tienda.agregar_producto(p2)

# Mostrar productos
tienda.mostrar_productos()

# Vender un producto
tienda.vender("Huevos")
