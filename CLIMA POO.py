class RegistroClima:
    def __init__(self):
        self._temperaturas = []

    def ingresar_temperatura(self, temperatura):
        self._temperaturas.append(temperatura)

    def calcular_promedio(self):
        return sum(self._temperaturas) / len(self._temperaturas)


class ClimaSemanal(RegistroClima):
    def ingresar_datos_semanales(self):
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.ingresar_temperatura(temp)


def main():
    clima = ClimaSemanal()
    clima.ingresar_datos_semanales()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")


# Ejecución del programa
main()
