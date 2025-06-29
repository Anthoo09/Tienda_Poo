# Programa para calcular el área de un rectángulo y convertir unidades
# Autor: [Tu Nombre]
# Fecha: [Fecha]
# Este programa solicita al usuario la base y la altura de un rectángulo,
# calcula su área en metros cuadrados, convierte esa área a centímetros cuadrados,
# y muestra los resultados. Además verifica si el área es mayor que un valor dado.

def calcular_area_rectangulo(base_metros: float, altura_metros: float) -> float:
    """
    Calcula el área de un rectángulo en metros cuadrados.
    """
    return base_metros * altura_metros

def convertir_a_centimetros_cuadrados(area_m2: float) -> float:
    """
    Convierte un área de metros cuadrados a centímetros cuadrados.
    """
    return area_m2 * 10000  # 1 m² = 10,000 cm²

def es_area_grande(area_m2: float, umbral: float = 50.0) -> bool:
    """
    Determina si el área es mayor que un umbral dado.
    """
    return area_m2 > umbral

def main():
    print("Calculadora de área de rectángulo")

    # Solicitar datos al usuario
    base_metros = float(input("Ingrese la base en metros: "))
    altura_metros = float(input("Ingrese la altura en metros: "))

    # Calcular área
    area_m2 = calcular_area_rectangulo(base_metros, altura_metros)
    area_cm2 = convertir_a_centimetros_cuadrados(area_m2)
    area_grande = es_area_grande(area_m2)

    # Mostrar resultados
    print(f"\nEl área del rectángulo es: {area_m2} metros cuadrados")
    print(f"El área del rectángulo en centímetros cuadrados es: {area_cm2} cm²")

    if area_grande:
        print("El área es mayor que 50 metros cuadrados.")
    else:
        print("El área es menor o igual que 50 metros cuadrados.")

if __name__ == "__main__":
    main()
