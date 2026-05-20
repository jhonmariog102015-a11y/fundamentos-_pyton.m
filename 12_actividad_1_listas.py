# ==============================================================================
# ARCHIVO 12 — Actividad 1: Inventario de la Tienda Escolar
# TEMA: Creación de múltiples listas relacionadas, len() y type()
# ==============================================================================
# DESCRIPCIÓN DEL EJERCICIO:
#   Se crean tres listas paralelas (productos, precios, cantidades).
#   Cada índice representa el mismo artículo en las tres listas.
#   Se practica len(), type(), indexación y f-strings para mostrar datos.
# ==============================================================================

# ── PASO 1: Declarar las tres listas del inventario ───────────────────────────
# lista_productos → nombres de los artículos (tipo str)
# lista_precios   → precio de cada artículo en pesos (tipo int)
# lista_cantidades→ unidades disponibles de cada artículo (tipo int)
#
# IMPORTANTE: Las tres listas deben tener la MISMA cantidad de elementos.
# El índice 0 corresponde al mismo producto en las tres listas.
lista_productos  = ["cuadernos", "lapiceros", "gomas", "reglas", "colores", "pegamento"]
lista_precios    = [2500, 1200, 5000, 1000, 3000, 1500]
lista_cantidades = [100, 200, 150, 80, 50, 120]

# ── PASO 2: Usar len() para contar el número de productos ────────────────────
# len(lista) → devuelve el número de elementos que contiene la lista
cantidad_productos = len(lista_productos)  # Resultado: 6

# ── PASO 3: Imprimir el inventario completo con un solo print() ───────────────
# Se usan varias f-strings encadenadas (sin coma) dentro de un mismo print().
# \n genera un salto de línea dentro del texto.
print("inventario de la tienda escolar:"
      f"\nProductos: {lista_productos}"
      f"\nPrecios: {lista_precios}"
      f"\nCantidades: {lista_cantidades}"
      f"\nCantidad de productos en el inventario: {cantidad_productos}")

# ── PASO 4: Acceder a cada producto por su índice ─────────────────────────────
# Se usa lista[índice] para obtener el valor en una posición específica.
# El índice 0 es el primer elemento, 1 el segundo, y así sucesivamente.

# Índice 0 → cuadernos
print(f"El precio del cuaderno es: {lista_precios[0]} y su cantidad disponible es: {lista_cantidades[0]}")
# Índice 1 → lapiceros
print(f"El precio del lapicero es: {lista_precios[1]} y su cantidad disponible es: {lista_cantidades[1]}")
# Índice 2 → gomas
print(f"El precio de la goma es: {lista_precios[2]} y su cantidad disponible es: {lista_cantidades[2]}")
# Índice 3 → reglas
print(f"El precio de la regla es: {lista_precios[3]} y su cantidad disponible es: {lista_cantidades[3]}")
# Índice 4 → colores
print(f"El precio de los colores es: {lista_precios[4]} y su cantidad disponible es: {lista_cantidades[4]}")
# Índice 5 → pegamento
print(f"El precio del pegamento es: {lista_precios[5]} y su cantidad disponible es: {lista_cantidades[5]}")

# ── PASO 5: Verificar tipos de datos con type() ───────────────────────────────
# type(lista_productos)    → pregunta: ¿qué tipo de objeto ES la lista?
#                            Respuesta: <class 'list'>
print(type(lista_productos))    # <class 'list'> → indica que es una lista

# type(lista_productos[0]) → pregunta: ¿qué tipo de dato tiene el elemento 0?
#                            Respuesta: <class 'str'>
print(type(lista_productos[0])) # <class 'str'> → el primer elemento es un string (texto)

# DIFERENCIA CLAVE:
#   type(lista)    → nos dice que el CONTENEDOR es una lista
#   type(lista[0]) → nos dice el tipo del CONTENIDO (elemento individual)
