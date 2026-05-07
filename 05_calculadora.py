# ============================================================
#   EJERCICIO 5: Calculadora básica con menú
# ============================================================
# El usuario ingresa dos números y elige una operación
# matemática. Se usa if/elif para seleccionar la operación
# según el número que el usuario digitó en el menú.
#
# se agrega manejo del caso en que el
# usuario intente dividir por cero, mostrando un mensaje
# claro en lugar de lanzar un error.
# ============================================================

print("=" * 40)
print("       CALCULADORA BÁSICA")
print("=" * 40)

valor_1 = float(input("\n  Ingresa el primer número : "))
valor_2 = float(input("  Ingresa el segundo número: "))

print("""
  ¿Qué operación deseas realizar?
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
""")
tipo_operacion = input("  Elige una opción (1-4): ")

print("\n" + "-" * 40)

if tipo_operacion == "1":
    resultado = valor_1 + valor_2
    print(f"  {valor_1} + {valor_2} = {resultado}")

elif tipo_operacion == "2":
    resultado = valor_1 - valor_2
    print(f"  {valor_1} - {valor_2} = {resultado}")

elif tipo_operacion == "3":
    resultado = valor_1 * valor_2
    print(f"  {valor_1} × {valor_2} = {resultado}")

elif tipo_operacion == "4":
    # División: hay que validar que el divisor no sea cero
    if valor_2 != 0:
        resultado = valor_1 / valor_2
        print(f"  {valor_1} ÷ {valor_2} = {resultado:.4f}")
    else:
        print("  ⚠  No es posible dividir entre cero.")

else:
    print("  Opción no válida. Elige un número del 1 al 4.")

print("-" * 40)
