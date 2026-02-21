import os

class Producto:
    """
    Clase que representa un producto dentro del inventario.
    """
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    """
    Clase que gestiona el inventario completo.
    Maneja almacenamiento y recuperación desde archivo.
    """
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga los productos desde el archivo.
        Si el archivo no existe, lo crea automáticamente.
        Maneja posibles errores de lectura y corrupción.
        """
        try:
            if not os.path.exists(self.archivo):
                # Crear archivo vacío si no existe
                with open(self.archivo, "w") as f:
                    pass
                print("Archivo de inventario creado correctamente.")
                return

            with open(self.archivo, "r") as f:
                for linea in f:
                    try:
                        id_producto, nombre, cantidad, precio = linea.strip().split(",")
                        self.productos[id_producto] = Producto(
                            id_producto,
                            nombre,
                            int(cantidad),
                            float(precio)
                        )
                    except ValueError:
                        print("Advertencia: Línea corrupta ignorada en el archivo.")

            print("Inventario cargado correctamente.")

        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):
        """
        Guarda todos los productos en el archivo.
        Maneja errores de escritura.
        """
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(str(producto) + "\n")
            print("Inventario guardado exitosamente en el archivo.")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """
        Agrega un nuevo producto al inventario.
        """
        if id_producto in self.productos:
            print("Error: El producto ya existe.")
            return

        self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
        self.guardar_inventario()
        print("Producto agregado correctamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza cantidad o precio de un producto existente.
        """
        if id_producto not in self.productos:
            print("Error: Producto no encontrado.")
            return

        if cantidad is not None:
            self.productos[id_producto].cantidad = cantidad
        if precio is not None:
            self.productos[id_producto].precio = precio

        self.guardar_inventario()
        print("Producto actualizado correctamente.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario.
        """
        if id_producto not in self.productos:
            print("Error: Producto no encontrado.")
            return

        del self.productos[id_producto]
        self.guardar_inventario()
        print("Producto eliminado correctamente.")

    def mostrar_inventario(self):
        """
        Muestra todos los productos del inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("\n--- Inventario Actual ---")
        for producto in self.productos.values():
            print(f"ID: {producto.id} | Nombre: {producto.nombre} | "
                  f"Cantidad: {producto.cantidad} | Precio: ${producto.precio}")
        print("--------------------------\n")


def menu():
    inventario = Inventario()

    while True:
        print("\n=== Sistema de Gestión de Inventarios ===")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(id_producto, nombre, cantidad, precio)
            except ValueError:
                print("Error: Cantidad o precio inválido.")

        elif opcion == "2":
            id_producto = input("ID del producto a actualizar: ")
            try:
                cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
                precio = input("Nuevo precio (dejar vacío si no cambia): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error: Datos inválidos.")

        elif opcion == "3":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()