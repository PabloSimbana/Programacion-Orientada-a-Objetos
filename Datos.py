# -------------------------------------------------------------
# Programa que calcula el área de un rectángulo y muestra
# información básica del usuario, utilizando distintos tipos
# de datos y una función para realizar el cálculo.
# -------------------------------------------------------------

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo multiplicando
    la base por la altura.
    :param base: float que representa la base del rectángulo
    :param altura: float que representa la altura del rectángulo
    :return: float con el área calculada
    """
    return base * altura


# Datos del usuario (tipo string e int)
nombre_usuario = "Carlos"      # Nombre del usuario
edad_usuario = 20              # Edad del usuario

# Datos del rectángulo (tipo float)
base_rectangulo = 5.5          # Base del rectángulo
altura_rectangulo = 3.2        # Altura del rectángulo

# Llamada a la función para calcular el área
area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)

# Evaluación lógica para determinar si el área es grande
# El resultado será True o False (tipo boolean)
area_es_grande = area_rectangulo > 15

# Mostrar los datos y resultados por pantalla
print("Nombre del usuario:", nombre_usuario)
print("Edad:", edad_usuario)
print("Base del rectángulo:", base_rectangulo)
print("Altura del rectángulo:", altura_rectangulo)
print("Área del rectángulo:", area_rectangulo)

# Condicional que evalúa el valor booleano
if area_es_grande:
    print("El área del rectángulo es grande.")
else:
    print("El área del rectángulo es pequeña.")
