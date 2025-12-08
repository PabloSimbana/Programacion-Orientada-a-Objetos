class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método que representa la acción esencial de un auto
    def encender(self):
        return "El auto está encendido."