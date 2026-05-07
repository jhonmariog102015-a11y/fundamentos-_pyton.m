# ============================================================
#   EJERCICIO 2: Operadores aritméticos y precedencia
# ============================================================
# Se practican todos los operadores matemáticos de Python:
#   +   suma              -   resta
#   *   multiplicación    /   división real
#   //  división entera   %   módulo (residuo)
#   **  potencia
#
# También se estudia la precedencia (orden de evaluación):
# Python sigue el orden PEMDAS: Potencia > * / > + -
# Los paréntesis siempre tienen la mayor prioridad.
# ============================================================

import math  # módulo estándar con funciones matemáticas avanzadas

a = 5
b = 6

print("=" * 45)
print(f"OPERADORES ARITMÉTICOS(a={a}, b={b})")
print("=" * 45)

# Operaciones básicas
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b  # devuelve float aunque el resultado sea entero
division_entera = a // b  # descarta la parte decimal (trunca hacia abajo)
modulo = a % b  # residuo de la división
potencia = a ** b  # a elevado a la b

print(f"{a} + {b} = {suma}")
print(f"{a} - {b} = {resta}")
print(f"{a} * {b} = {multiplicacion}")
print(f"{a} / {b} = {division:.4f}")
print(f"{a} // {b} = {division_entera}  ← parte entera")
print(f"{a} % {b} = {modulo}   ← residuo")
print(f"{a} ** {b} = {potencia}  ← potencia")

# --- Precedencia de operadores ---
print("\n" + "=" * 45)
print("PRECEDENCIA DE OPERADORES")
print("=" * 45)

# Sin paréntesis: primero * , luego +
r1 = a + b * 2
print(f"{a} + {b} * 2 = {r1} (primero {b} * 2 = {b*2}, luego + {a})")

# Con paréntesis: forzamos que + sea primero
r2 = (a + b) * 2
print(f"({a} + {b}) * 2 = {r2} (primero {a} + {b} = {a+b}, luego * 2)")

# División entera vs agrupación
r3 = a * b // 3
print(f"{a} * {b} // 3 = {r3} ({a} * {b} = {a*b}, luego // {3})")

r4 = a * (b // 3)
print(f"{a} * ({b} // 3) = {r4} ({b} // 3 = {b//3}, luego * {a})")

# Ejercicio de precedencia complejo:  5 + 3 * 2^2 = 5 + 3*4 = 5 + 12 = 17
ejercicio = 5 + 3 * 2 ** 2
print(f"\n  5+3*2**2= {ejercicio}  (2**2=4, luego 3*4=12, luego 5+12)")

# --- Operador walrus := (asignación dentro de expresión) ---
print("\n" + "=" * 45)
print("OPERADOR WALRUS:=")
print("=" * 45)
# Asigna el valor 10 a x Y lo imprime en la misma línea
print(f"  print(x := 10) →", (x := 10))

# --- Función matemática de la biblioteca math ---
print("\n" + "=" * 45)
print("   FUNCIÓN math.sqrt()")
print("=" * 45)
print(f"  math.sqrt(16) = {math.sqrt(16)}  ← raíz cuadrada de 16")
