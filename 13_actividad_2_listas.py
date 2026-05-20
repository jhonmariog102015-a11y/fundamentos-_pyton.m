# ==============================================================================
# ARCHIVO 13 — Actividad 2: Análisis de Temperaturas Semanales
# TEMA: Indexación positiva/negativa, slicing y cálculo de promedios
# ==============================================================================
# DESCRIPCIÓN DEL EJERCICIO:
#   Se trabaja con una lista de 14 temperaturas (dos semanas).
#   Se practica acceder a elementos por índice positivo y negativo,
#   extraer sublistas con slicing, calcular promedios y comparar resultados.
# ==============================================================================

# ── PASO 1: Declarar la lista de temperaturas (14 días) ──────────────────────
# Cada número es la temperatura de un día (en grados Celsius).
# El índice va del 0 (día 1) al 13 (día 14).
temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]
#  índice:       0   1   2   3   4   5   6   7   8   9  10  11  12  13

# ── PASO 2: Indexación positiva y negativa ────────────────────────────────────
# Índice POSITIVO → cuenta desde el inicio (0 = primer elemento)
# Índice NEGATIVO → cuenta desde el final (-1 = último elemento)

print(f"Temperatura del primer día: {temperaturas[0]}°C")     # índice 0  → 18
print(f"Temperatura del último día: {temperaturas[-1]}°C")    # índice -1 → 19
print(f"Temperatura del día 7: {temperaturas[6]}°C")          # índice 6  → 17 (día 7, ya que empieza en 0)
print(f"Temperatura del penúltimo día: {temperaturas[-2]}°C") # índice -2 → 22

# ── PASO 3: Slicing → extraer sublistas ───────────────────────────────────────
# SINTAXIS: lista[inicio : fin : paso]
#   - inicio → índice donde empieza el corte (incluido)
#   - fin    → índice donde termina el corte (NO incluido)
#   - paso   → de cuánto en cuánto avanza (cada 2 = saltar un elemento)

# Primera semana con paso 2 → toma días de índice 0, 2, 4, 6
print(f"Temperaturas de la primera semana: {temperaturas[0:7:2]}")

# Segunda semana con paso 2 → toma días de índice 7, 9, 11, 13
print(f"Temperaturas de la segunda semana: {temperaturas[7:14:2]}")

# Solo días pares → empieza en índice 1 (día 2), salta de 2 en 2
print(f"Temperaturas de los días pares: {temperaturas[1::2]}")

# Lista invertida → paso -1 recorre la lista de atrás hacia adelante
print(f"Temperaturas en orden invertido: {temperaturas[::-1]}")

# ── PASO 4: Calcular promedios con sum() y len() ──────────────────────────────
# FÓRMULA: promedio = suma de todos los elementos / cantidad de elementos
#   sum(lista) → suma todos los valores
#   len(lista) → cuenta cuántos valores hay

# Promedio de la primera semana (sobre los días seleccionados con slicing)
promedio_primera_semana = sum(temperaturas[0:7:2]) / len(temperaturas[0:7:2])

# Promedio de la segunda semana (sobre los días seleccionados con slicing)
promedio_segunda_semana = sum(temperaturas[7:14:2]) / len(temperaturas[7:14:2])

# Se imprimen con 2 decimales usando el formato :.2f dentro del f-string
print(f"Temperatura promedio de la primera semana: {promedio_primera_semana:.2f}°C")
print(f"Temperatura promedio de la segunda semana: {promedio_segunda_semana:.2f}°C")

# ── PASO 5 (Bonus): Comparar promedios con if / elif / else ──────────────────
# Se comparan los dos promedios con el operador ">" (mayor que)
# Según el resultado, se muestra un mensaje descriptivo diferente

if promedio_primera_semana > promedio_segunda_semana:
    print("La primera semana tuvo una temperatura promedio mayor.")
elif promedio_segunda_semana > promedio_primera_semana:
    # Si la segunda es mayor, entra aquí
    print("La segunda semana tuvo una temperatura promedio mayor.")
else:
    # Si son iguales, entra aquí
    print("Ambas semanas tuvieron la misma temperatura promedio.")
