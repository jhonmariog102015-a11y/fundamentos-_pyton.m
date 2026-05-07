# ============================================================
#   EJERCICIO 9: Variables, valores y tipo de dato con type()
# ============================================================
# Ejercicios cortos de práctica con variables:
#   • Declaración de variables simples (eje.py)
#   • Leer un valor con input() y ver su tipo con type() (RDE.py)
#
# type() devuelve la clase del objeto:
#   <class 'str'>, <class 'int'>, <class 'float'>, etc.
# input() SIEMPRE devuelve str, por eso hay que convertir
# con int() o float() cuando se necesita trabajar con números.
# ============================================================

# --- Parte A: Variables simples (eje.py) ---
print("=" * 45)
print("   PARTE A: Variables de un juego")
print("=" * 45)

username = "zombie"  # str  → nombre del jugador
points = 50  # int  → puntos acumulados
lives = 3  # int  → vidas restantes

print(f"  Jugador  : {username}")
print(f"  Puntos   : {points}")
print(f"  Vidas    : {lives}")

# --- Parte B: input() y type() (RDE.py) ---
print("\n" + "=" * 45)
print("   PARTE B: Entrada del usuario y type()")
print("=" * 45)

# int() convierte el texto de input() a número entero
height = int(input("  Ingresa tu altura en cm: "))

# type() devuelve el tipo del objeto como clase
print(f"  Valor ingresado : {height}")
print(f"  Tipo de dato    : {type(height)}")  # → <class 'int'>

# Demostración: sin int(), input() devuelve str
height_str = input("  Ingresa de nuevo tu altura (sin convertir): ")
print(f"  Valor sin convertir : {height_str}")
print(f"  Tipo sin convertir  : {type(height_str)}")  # → <class 'str'>
