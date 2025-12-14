def ingresar_temperaturas():
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio_semanal(temperaturas):
    return sum(temperaturas) / len(temperaturas)


def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")


# Ejecución del programa
main()
