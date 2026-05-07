# ============================================================
#   EJERCICIO 7: Medidor de IMC con bucle while (Actividad 3)
# ============================================================
# El IMC (Índice de Masa Corporal) es un indicador de salud
# que se calcula con la fórmula:
#
#     IMC = peso (kg) / altura (m)²
#
# Clasificación según la OMS:
#   < 18.5           → Bajo peso
#   18.5 ≤ IMC < 25  → Peso normal (buena forma)
#   25   ≤ IMC < 30  → Sobrepeso
#   ≥ 30             → Obesidad
#
# Se usa un bucle while True para permitir calcular varios
# IMC sin reiniciar el programa. El bucle termina cuando el
# usuario responde "no" a la pregunta de continuar.
# ============================================================

def clasificar_imc(imc):
    """Devuelve la categoría de peso según el valor de IMC."""
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal (buena forma)"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


print("=" * 45)
print("        CALCULADORA DE IMC")
print("=" * 45)

while True:
    # Solicitar datos al usuario
    peso   = float(input("\n  Ingresa tu peso en kg   : "))
    altura = float(input("  Ingresa tu altura en m  : "))

    # Calcular el IMC con la fórmula: peso / altura²
    # El operador ** eleva a la potencia (altura**2 = altura²)
    imc = peso / altura ** 2
    imc_redondeado = round(imc, 2)

    # Obtener categoría de peso
    categoria = clasificar_imc(imc)

    # Mostrar resultado
    print("\n" + "-" * 45)
    print(f"Tu IMC es: {imc_redondeado}")
    print(f"Clasificación: {categoria}")
    print("-" * 45)

    # Preguntar si desea calcular otro IMC
    # .lower() convierte la respuesta a minúsculas para comparar con "si"
    respuesta = input("\n  ¿Deseas calcular otro IMC? (si / no): ")
    if respuesta.strip().lower() != "si":
        print("\n  Gracias por usar la calculadora de IMC. ¡Hasta luego!")
        break   # sale del bucle while y termina el programa
