# ============================================================
#   EJERCICIO 6: Calculadora de notas (Actividad 2)
# ============================================================
# El usuario ingresa tres notas parciales (escala 0.0 – 5.0).
# El programa calcula:
#   • El promedio de las tres notas.
#   • Los puntos que faltan para alcanzar la nota máxima (5.0).
#   • Si el estudiante aprueba (promedio ≥ 3.0) o reprueba.
#
# Se usan: variables float, operaciones aritméticas, round(),
# operadores de comparación y condicionales if/else.
# ============================================================

print("=" * 42)
print("CALCULADORA DE NOTAS")
print("=" * 42)
print("\n  Ingresa tus tres notas parciales (0.0 – 5.0):\n")

nota1 = float(input(" Nota parcial 1: "))
nota2 = float(input(" Nota parcial 2: "))
nota3 = float(input(" Nota parcial 3: "))

# Cálculo del promedio: suma de las tres notas dividida entre 3
promedio = (nota1 + nota2 + nota3) / 3
promedio = round(promedio, 2)   # redondeamos a 2 decimales

# Puntos que le faltan para llegar a 5.0
nota_maxima = 5.0
puntos_faltantes = round(nota_maxima - promedio, 2)

# Condición de aprobación: promedio mayor o igual a 3.0
aprueba = promedio >= 3.0

# --- Mostrar resultados ---
print("\n" + "=" * 42)
print("RESULTADOS")
print("=" * 42)
print(f"\n  Nota 1:  {nota1}")
print(f"  Nota 2: {nota2}")
print(f"  Nota 3: {nota3}")
print(f"\n  Promedio: {promedio}")
print(f"  Puntos para llegar a 5.0: {puntos_faltantes}")

print("\n" + "-" * 42)

if aprueba:
    print(f"Estado : ✔  APROBADO")
    print(f"¡Felicitaciones! Tu promedio de {promedio} es suficiente.")
else:
    print(f"Estado : ✘  REPROBADO")
    print(f"Tu promedio de {promedio} está por debajo de 3.0.")
    print(f"Necesitas subir {puntos_faltantes - (5.0 - 3.0):.2f} puntos para aprobar.")

print("\n" + "=" * 42)