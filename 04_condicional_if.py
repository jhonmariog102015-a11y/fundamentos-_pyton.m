# ============================================================
#   EJERCICIO 4: Condicionales if / elif / else
# ============================================================
# Las estructuras condicionales permiten ejecutar bloques de
# código solo cuando se cumple una condición.
#
#   if <condición>:      → se ejecuta si la condición es True
#   elif <condición>:    → se evalúa si la anterior fue False
#   else:                → se ejecuta cuando ninguna fue True
#
# También se estudia el operador ternario (if en una línea)
# y los if anidados con operadores lógicos (and / or).
# ============================================================

# --- 1. if / else básico ---
print("=" * 45)
print("   1. IF / ELSE BÁSICO")
print("=" * 45)

if False:
    print("Este bloque nunca se ejecuta (condición False)")
else:
    print("Se ejecuta el else porque la condición fue False")

# --- 2. if / elif / else (múltiples ramas) ---
print("\n" + "=" * 45)
print("   2. IF / ELIF / ELSE")
print("=" * 45)

if False:
    print("Primera condición: False → no entra")
elif False:
    print("Segunda condición: False → no entra")
elif True:
    print("Tercera condición: True  → ¡entra aquí!")
else:
    print("Este else solo se ejecutaría si todas fueran False")

# --- 3. if con variable numérica ---
print("\n" + "=" * 45)
print("   3. CLASIFICACIÓN POR EDAD (variable fija)")
print("=" * 45)

edad = 32
print(f"  Edad: {edad}")

if edad < 18:
    print("  → Menor de edad")
elif edad < 60:
    print("  → Adulto joven")
else:
    print("  → Adulto mayor")

# --- 4. if con operadores lógicos (and) ---
print("\n" + "=" * 45)
print("   4. IF CON OPERADOR LÓGICO 'and'")
print("=" * 45)
# 'and' exige que AMBAS condiciones sean True
año = 32
print(f"  Año: {año}")

if año < 18:
    print("  → Menor de edad")
elif año >= 18 and año < 60:
    print("  → Adulto joven  (18 ≤ año < 60)")
else:
    print("  → Adulto mayor  (60 o más)")

# --- 5. if con entrada del usuario ---
print("\n" + "=" * 45)
print("   5. IF CON INPUT DEL USUARIO")
print("=" * 45)

edad_usuario = int(input("  Ingresa tu edad: "))

if edad_usuario < 18:
    print("  → Eres menor de edad")
elif edad_usuario >= 18 and edad_usuario < 60:
    print("  → Eres un adulto joven")
else:
    print("  → Eres un adulto mayor")

# --- 6. Operador ternario (if en una sola línea) ---
print("\n" + "=" * 45)
print("   6. OPERADOR TERNARIO")
print("=" * 45)
# Sintaxis: <valor_si_true> if <condición> else <valor_si_false>

numero = 4
resultado = "par" if numero % 2 == 0 else "impar"
print(f"  {numero} es → {resultado}")

numero2 = 7
resultado2 = "par" if numero2 % 2 == 0 else "impar"
print(f"  {numero2} es → {resultado2}")
