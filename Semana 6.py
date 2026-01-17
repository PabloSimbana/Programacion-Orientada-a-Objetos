# Clase base
class Empleado:
    def __init__(self, nombre, salario):
        # Atributos encapsulados (privados)
        self.__nombre = nombre
        self.__salario = salario

    # Métodos getter (encapsulación)
    def get_nombre(self):
        return self.__nombre

    def get_salario(self):
        return self.__salario

    # Método que será sobrescrito (polimorfismo)
    def calcular_pago(self):
        return self.__salario


# Clase derivada (herencia)
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, salario, horas_trabajadas):
        super().__init__(nombre, salario)
        self.horas_trabajadas = horas_trabajadas

    # Sobrescritura del método (polimorfismo)
    def calcular_pago(self):
        return self.get_salario() * self.horas_trabajadas


# Otra clase derivada
class EmpleadoBono(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono

    # Sobrescritura del método (polimorfismo)
    def calcular_pago(self):
        return self.get_salario() + self.bono


# Programa principal
if __name__ == "__main__":
    # Creación de objetos
    empleado1 = Empleado("Ana", 1000)
    empleado2 = EmpleadoPorHoras("Luis", 20, 40)
    empleado3 = EmpleadoBono("María", 1200, 300)

    # Lista de empleados para demostrar polimorfismo
    empleados = [empleado1, empleado2, empleado3]

    # Uso de métodos
    for empleado in empleados:
        print(f"Empleado: {empleado.get_nombre()}")
        print(f"Pago total: {empleado.calcular_pago()}")
        print("-" * 30)
