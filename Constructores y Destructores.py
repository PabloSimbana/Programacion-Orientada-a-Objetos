class FileManager:
    """
    Clase que demuestra el uso de constructor (__init__) y destructor (__del__).
    Maneja la apertura y cierre de un archivo como recurso externo.
    """

    def __init__(self, filename, mode="w"):
        """
        Constructor: Se ejecuta cuando se crea el objeto.
        Inicializa los atributos y abre el archivo.
        """
        self.filename = filename
        self.mode = mode
        self.file = open(self.filename, self.mode)
        print(f"[INIT] Archivo '{self.filename}' abierto en modo '{self.mode}'.")

    def write_message(self, message):
        """
        Método para escribir contenido en el archivo.
        """
        if self.file:
            self.file.write(message + "\n")
            print("[WRITE] Mensaje escrito en el archivo.")

    def __del__(self):
        """
        Destructor: Se ejecuta cuando el objeto es eliminado
        o el programa finaliza.
        Libera el recurso cerrando el archivo.
        """
        if self.file:
            self.file.close()
            print(f"[DEL] Archivo '{self.filename}' cerrado correctamente.")


# ------------------------------
# Uso de la clase
# ------------------------------

if __name__ == "__main__":
    manager = FileManager("ejemplo.txt")
    manager.write_message("Hola, este archivo fue creado usando Python.")
    manager.write_message("El destructor cerrará el archivo automáticamente.")

    # Cuando el programa termine o manager sea eliminado,
    # se ejecutará el destructor (__del__)
