class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        return f"{self.nombre} está comiendo."


class Perro(Animal):
    def ladrar(self):
        return "Guau guau!"


class Gato(Animal):
    def maullar(self):
        return "Miau!"