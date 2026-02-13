class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def buscar_por_id(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None

    def agregar_producto(self, producto):
        if self.buscar_por_id(producto.get_id()) is not None:
            return False
        self.productos.append(producto)
        return True

    def eliminar_producto(self, id):
        producto = self.buscar_por_id(id)
        if producto:
            self.productos.remove(producto)
            return True
        return False

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        producto = self.buscar_por_id(id)
        if producto:
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            return True
        return False

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def main():
    inventario = Inventario()

    while True:
        print("\n=== SISTEMA DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                nuevo = Producto(id, nombre, cantidad, precio)
                if inventario.agregar_producto(nuevo):
                    print("Producto agregado correctamente.")
                else:
                    print("Error: El ID ya existe.")
            except ValueError:
                print("Error: Entrada inválida.")

        elif opcion == "2":
            try:
                id = int(input("Ingrese ID a eliminar: "))
                if inventario.eliminar_producto(id):
                    print("Producto eliminado.")
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "3":
            try:
                id = int(input("Ingrese ID a actualizar: "))
                nueva_cantidad = int(input("Nueva cantidad: "))
                nuevo_precio = float(input("Nuevo precio: "))
                if inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio):
                    print("Producto actualizado.")
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("Entrada inválida.")

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
