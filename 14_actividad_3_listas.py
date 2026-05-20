# ==============================================================================
# ARCHIVO 14 — Actividad 3: Gestión de Lista de Reproducción Musical
# TEMA: Métodos de modificación y consulta de listas
# ==============================================================================
# DESCRIPCIÓN DEL EJERCICIO:
#   Se gestiona una playlist musical aplicando los métodos: append, insert,
#   extend, remove, pop y sort. Al final se consulta la lista con len(),
#   index() y count() para responder preguntas sobre el estado de la playlist.
# ==============================================================================

# ── PASO 1: Declarar la playlist inicial con 5 canciones ─────────────────────
# Se crea la lista con 5 nombres de canciones (tipo str)
canciones = ["cuatro babys,", "mala fama", "la jeepeta", "safaera", "yo perreo sola"]
print(canciones)  # Estado inicial de la playlist

# ── PASO 2: .append() → Agregar una canción al FINAL de la lista ──────────────
# .append(valor) siempre añade el elemento como el ÚLTIMO de la lista
canciones.append("tusa")
print(canciones)  # "tusa" queda al final → 6 canciones en total

# ── PASO 3: .insert() → Insertar en la SEGUNDA posición (índice 1) ───────────
# .insert(índice, valor) inserta el valor en la posición indicada.
# Los elementos desde esa posición en adelante se desplazan a la derecha.
canciones.insert(1, "callaita")
print(canciones)  # "callaita" queda en el índice 1 → 7 canciones en total

# ── PASO 4: .extend() → Fusionar otra lista al final ─────────────────────────
# .extend(otra_lista) agrega TODOS los elementos de otra lista uno por uno.
# DIFERENCIA con append: append(["a","b"]) añade la lista como un solo elemento,
#                        extend(["a","b"]) añade "a" y "b" como dos elementos.
canciones.extend(["Bonus Track 1", "Bonus Track 2"])
print(canciones)  # Se agregan los 2 bonus tracks → 9 canciones en total

# ── PASO 5: .remove() → Eliminar una canción por su nombre  **
# .remove(valor) elimina la PRIMERA aparición del valor en la lista.
# Si el valor no existe, Python lanza un ValueError (error de valor).
canciones.remove("mala fama")
print(canciones)  # "mala fama" fue eliminada → 8 canciones

# ── PASO 6: .pop() → Eliminar la ÚLTIMA canción y guardar su valor ────────────
# .pop() sin argumentos → elimina y RETORNA el último elemento de la lista.
# El valor eliminado se guarda en una variable para poder usarlo luego.
ultima_cancion = canciones.pop()
print(f"la ultima cancion eliminada es: {ultima_cancion}")  # Muestra qué se eliminó
print(canciones)  # → 7 canciones restantes

# ── PASO 7: .sort() → Ordenar la playlist alfabéticamente ────────────────────
# .sort() ordena la lista en orden ALFABÉTICO (A → Z).
# Nota: Las letras MAYÚSCULAS tienen prioridad sobre las minúsculas.
# Esta operación modifica la lista ORIGINAL (no crea una nueva lista).
canciones.sort()
print(canciones)  # Playlist ordenada de la A a la Z

# ── PASO 8: Consultas finales con len(), .index() y .count() ──────────────────

# Pregunta 1: ¿Cuántas canciones tiene la playlist?
# len(lista) → devuelve el número total de elementos
cantidad_canciones = len(canciones)
print(f"la cantidad de canciones en la playlist es: {cantidad_canciones}")

# Pregunta 2: ¿En qué posición está "cuatro babys,"?
# .index(valor) → devuelve el índice de la primera ocurrencia del valor
posicion_cuatro_babys = canciones.index("cuatro babys,")
print(f"la posicion de la cancion cuatro babys es: {posicion_cuatro_babys}")

# Pregunta 3: ¿Cuántas veces aparece "Bonus Track 1" en la playlist?
# .count(valor) → cuenta las veces que aparece el valor en la lista
cantidad_bonus_track_1 = canciones.count("Bonus Track 1")
print(f"la cantidad de veces que aparece Bonus Track 1 es: {cantidad_bonus_track_1}")
