# ==============================================================================
# ARCHIVO 11 — Introducción a las Listas en Python
# TEMA: Estructura, creación y métodos básicos de listas
# ==============================================================================

# ── PASO 1: Crear una lista básica ───────────────────────────────────────────
# Una lista se define con corchetes []. El índice empieza siempre en 0.
#   índice →   0          1          2
Listas = ["objeto1", "objeto2", "objeto3"]
print(type(Listas))  # <class 'list'> → confirma que es una lista

# ── PASO 2: Lista mixta ───────────────────────────────────────────────────────
# Python permite listas con distintos tipos de datos: str, int, float, bool
lista_mixta = {"Hola", 123, 3.14, True}  # Nota: esto es un SET (conjunto), no lista

# ── PASO 3: Lista de aprendices SENA ─────────────────────────────────────────
# Se declara la lista principal con cuatro nombres de aprendices
aprendices = ["Andres", "Camilo", "Sofia", "Valentina"]
print(aprendices)  # Muestra la lista completa

# Se pueden crear otras variables que apuntan al mismo contenido
Aprendices_212 = ["Andres", "Camilo", "Sofia", "Valentina"]
apredices_212  = ["Andres", "Camilo", "Sofia", "Valentina"]

# Asignar con "=" hace que ambas variables apunten al MISMO objeto en memoria
aprendices_212 = aprendices
print(aprendices_212)  # Misma lista que 'aprendices'

# ── PASO 4: Método .count() ───────────────────────────────────────────────────
# .count(valor) → cuenta cuántas veces aparece un elemento en la lista
count = aprendices.count("Andres")
print(aprendices.count("Andres"))   # 1 → "Andres" aparece una vez

print(aprendices.count("Camilo"))   # 1 → "Camilo" aparece una vez
count = aprendices.count("Camilo")
print(f"el nombre de camilo es: {count}")  # Usando f-string para mostrar el resultado

# También podemos usar .count() directamente dentro del f-string:
print(f"el nombre de sofia es: {aprendices.count('Sofia')}")
print(f"el nombre de valentina es: {aprendices.count('Valentina')}")

# ── PASO 5: Método .copy() ────────────────────────────────────────────────────
# .copy() crea una copia INDEPENDIENTE de la lista.
# Los cambios en nueva_lista NO afectarán a la lista original 'aprendices'
nueva_lista = aprendices.copy()
print(nueva_lista)

# ── PASO 6: Método .index() ───────────────────────────────────────────────────
# .index(valor) → devuelve el índice (posición) del elemento buscado
indice_valentina = aprendices.index("Valentina")
print(f"El índice de Valentina es: {indice_valentina}")  # 3

# ── PASO 7: Método .append() → Agregar al final ───────────────────────────────
# .append(valor) → agrega un elemento al FINAL de la lista
nueva_lista.append("Santiago")
print(nueva_lista)  # ['Andres', 'Camilo', 'Sofia', 'Valentina', 'Santiago']

# ── PASO 8: Método .insert() → Insertar en posición específica ───────────────
# .insert(índice, valor) → inserta en la posición indicada y desplaza los demás
nueva_lista.insert(2, "Maria")
print(nueva_lista)  # María queda en la posición 2

# Se repiten los métodos para demostrar el acumulado de cambios
nueva_lista.append("Santiago")
nueva_lista.insert(2, "Maria")
print(nueva_lista)  # Lista con los dos "Santiago" y dos "Maria"

# ── PASO 9: Método .remove() → Eliminar por valor ────────────────────────────
# .remove(valor) → elimina la PRIMERA ocurrencia del valor indicado
nueva_lista.remove("Santiago")
print(nueva_lista)

# ── PASO 10: Método .pop() → Eliminar por índice ─────────────────────────────
# .pop(índice) → elimina y retorna el elemento de la posición indicada
nueva_lista.pop(2)
print(nueva_lista)

nueva_lista.insert  # ← Esta línea no tiene efecto (falta llamada con paréntesis)

# ── PASO 11: Operador 'in' → Verificar si un elemento existe ─────────────────
# 'in' devuelve True si el elemento está en la lista, False si no está
if "Maria" in nueva_lista:
    print("Maria esta en la lista")
else:
    print("Maria no esta en la lista")

# ── PASO 12: Método .sort() → Ordenar la lista ───────────────────────────────
# .sort() ordena la lista ALFABÉTICAMENTE (A → Z) o de menor a mayor
nueva_lista.sort()
print(nueva_lista)

# ── PASO 13: Método .reverse() → Invertir el orden ───────────────────────────
# .reverse() invierte el orden ACTUAL de la lista (no ordena, solo voltea)
nueva_lista.reverse()
print(nueva_lista)