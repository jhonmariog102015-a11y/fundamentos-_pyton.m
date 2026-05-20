"""
================================================================================
   DOCUMENTO EXPLICATIVO - FUNDAMENTOS DE PYTHON
   Tema: LISTAS EN PYTHON (Archivos 11 al 14)
   Autor: Estudiante SENA
   Fecha: 2026
================================================================================

Este documento explica de forma clara y ordenada los conceptos y ejercicios
trabajados en los archivos 11_Listas.py, 12_actividad_1_listas.py,
13_actividad_2_listas.py y 14_actividad_3_listas.py.

Cada sección puede copiarse y pegarse directamente en un documento Word
o presentación para su entrega académica.
================================================================================
"""

# ==============================================================================
# ¿QUÉ ES UNA LISTA EN PYTHON?
# ==============================================================================
"""
Una LISTA en Python es una estructura de datos que permite almacenar múltiples
valores en una sola variable. Las listas:

  - Se definen usando corchetes: [ ]
  - Pueden contener distintos tipos de datos: strings, enteros, floats, booleanos
  - Son ORDENADAS: cada elemento tiene una posición (índice), que empieza en 0
  - Son MUTABLES: se pueden modificar (agregar, eliminar, cambiar elementos)
  - Permiten elementos DUPLICADOS

SINTAXIS BÁSICA:
    mi_lista = [elemento0, elemento1, elemento2]

EJEMPLO:
    frutas = ["manzana", "pera", "uva"]
    #  índice:     0          1       2

Para acceder a un elemento se usa su índice:
    frutas[0]  →  "manzana"
    frutas[-1] →  "uva"  (índice negativo: desde el final)
"""

# ==============================================================================
# ARCHIVO 11 — 11_Listas.py
# TEMA: INTRODUCCIÓN A LAS LISTAS Y SUS MÉTODOS PRINCIPALES
# ==============================================================================
"""
OBJETIVO DEL ARCHIVO:
    Presentar la estructura de una lista, cómo se crea, cómo se accede a sus
    elementos y los métodos más importantes para manipularla.

─────────────────────────────────────────────────────────────────────────────
PASO 1 — CREAR UNA LISTA BÁSICA
─────────────────────────────────────────────────────────────────────────────
    Listas = ["objeto1", "objeto2", "objeto3"]
    print(type(Listas))   # Salida: <class 'list'>

    ► Se crea una lista con tres elementos de tipo string.
    ► type() nos dice que es un objeto de clase 'list'.

─────────────────────────────────────────────────────────────────────────────
PASO 2 — LISTA DE APRENDICES
─────────────────────────────────────────────────────────────────────────────
    aprendices = ["Andres", "Camilo", "Sofia", "Valentina"]
    print(aprendices)
    # Salida: ['Andres', 'Camilo', 'Sofia', 'Valentina']

    ► Lista con nombres de aprendices del SENA.
    ► Se puede asignar una lista a otra variable (ambas apuntan al mismo objeto):
        aprendices_212 = aprendices

─────────────────────────────────────────────────────────────────────────────
PASO 3 — MÉTODO .count()
─────────────────────────────────────────────────────────────────────────────
    .count(valor)  →  Cuenta cuántas veces aparece un elemento en la lista.

    EJEMPLO:
        aprendices.count("Andres")   →  1
        aprendices.count("Camilo")   →  1

    Se puede usar directamente en un print() con f-string:
        print(f"el nombre de camilo es: {aprendices.count('Camilo')}")

─────────────────────────────────────────────────────────────────────────────
PASO 4 — MÉTODO .copy()
─────────────────────────────────────────────────────────────────────────────
    .copy()  →  Crea una COPIA INDEPENDIENTE de la lista.

    EJEMPLO:
        nueva_lista = aprendices.copy()

    ► A diferencia de asignar con "=", .copy() crea un objeto separado.
      Los cambios en nueva_lista NO afectan a aprendices.

─────────────────────────────────────────────────────────────────────────────
PASO 5 — MÉTODO .index()
─────────────────────────────────────────────────────────────────────────────
    .index(valor)  →  Devuelve el índice (posición) de un elemento.

    EJEMPLO:
        indice_valentina = aprendices.index("Valentina")
        print(f"El índice de Valentina es: {indice_valentina}")
        # Salida: El índice de Valentina es: 3

─────────────────────────────────────────────────────────────────────────────
PASO 6 — MÉTODO .append() e .insert()
─────────────────────────────────────────────────────────────────────────────
    .append(valor)        →  Agrega un elemento AL FINAL de la lista.
    .insert(índice, valor) →  Inserta un elemento en una POSICIÓN específica.

    EJEMPLO:
        nueva_lista.append("Santiago")   # Agrega al final
        nueva_lista.insert(2, "Maria")   # Inserta en la posición 2

─────────────────────────────────────────────────────────────────────────────
PASO 7 — MÉTODO .remove() y .pop()
─────────────────────────────────────────────────────────────────────────────
    .remove(valor)  →  Elimina la PRIMERA ocurrencia del valor indicado.
    .pop(índice)    →  Elimina el elemento en la posición indicada
                       (si no se da índice, elimina el último).

    EJEMPLO:
        nueva_lista.remove("Santiago")  # Elimina "Santiago"
        nueva_lista.pop(2)              # Elimina el elemento en posición 2

─────────────────────────────────────────────────────────────────────────────
PASO 8 — OPERADOR 'in' (VERIFICAR PERTENENCIA)
─────────────────────────────────────────────────────────────────────────────
    El operador 'in' verifica si un elemento existe en la lista.
    Devuelve True o False.

    EJEMPLO:
        if "Maria" in nueva_lista:
            print("Maria esta en la lista")
        else:
            print("Maria no esta en la lista")

─────────────────────────────────────────────────────────────────────────────
PASO 9 — MÉTODOS .sort() y .reverse()
─────────────────────────────────────────────────────────────────────────────
    .sort()     →  Ordena la lista ALFABÉTICAMENTE (A → Z) o de menor a mayor.
    .reverse()  →  Invierte el orden actual de la lista.

    EJEMPLO:
        nueva_lista.sort()    # ['Andres', 'Camilo', 'Maria', 'Sofia', 'Valentina']
        nueva_lista.reverse() # ['Valentina', 'Sofia', 'Maria', 'Camilo', 'Andres']
"""

# ==============================================================================
# ARCHIVO 12 — 12_actividad_1_listas.py
# TEMA: INVENTARIO DE UNA TIENDA ESCOLAR
# ==============================================================================
"""
OBJETIVO DEL EJERCICIO:
    Practicar la creación de múltiples listas relacionadas entre sí y el uso
    de indexación, len() y type() para consultar información del inventario.

─────────────────────────────────────────────────────────────────────────────
PASO 1 — DECLARAR LAS TRES LISTAS DEL INVENTARIO
─────────────────────────────────────────────────────────────────────────────
    lista_productos  = ["cuadernos", "lapiceros", "gomas", "reglas", "colores", "pegamento"]
    lista_precios    = [2500, 1200, 5000, 1000, 3000, 1500]
    lista_cantidades = [100, 200, 150, 80, 50, 120]

    ► Cada posición (índice) de las tres listas corresponde al mismo artículo.
      Ejemplo: el producto en el índice 0 ("cuadernos") cuesta 2500 y hay 100.

─────────────────────────────────────────────────────────────────────────────
PASO 2 — USAR len() PARA CONTAR PRODUCTOS
─────────────────────────────────────────────────────────────────────────────
    len(lista)  →  Devuelve el número de elementos que tiene la lista.

    EJEMPLO:
        cantidad_productos = len(lista_productos)
        # Resultado: 6

─────────────────────────────────────────────────────────────────────────────
PASO 3 — IMPRIMIR EL INVENTARIO COMPLETO
─────────────────────────────────────────────────────────────────────────────
    print("inventario de la tienda escolar:"
          f"\nProductos: {lista_productos}"
          f"\nPrecios: {lista_precios}"
          f"\nCantidades: {lista_cantidades}"
          f"\nCantidad de productos en el inventario: {cantidad_productos}")

    ► Se usa un solo print() con múltiples f-strings concatenadas (sin coma).
    ► \n crea un salto de línea dentro del texto.

─────────────────────────────────────────────────────────────────────────────
PASO 4 — ACCEDER A CADA PRODUCTO POR SU ÍNDICE
─────────────────────────────────────────────────────────────────────────────
    EJEMPLO:
        print(f"El precio del cuaderno es: {lista_precios[0]} y su cantidad disponible es: {lista_cantidades[0]}")

    ► lista_precios[0]    →  2500
    ► lista_cantidades[0] →  100

    Se repite este patrón para cada uno de los 6 artículos (índices 0 al 5).

─────────────────────────────────────────────────────────────────────────────
PASO 5 — VERIFICAR EL TIPO DE DATO CON type()
─────────────────────────────────────────────────────────────────────────────
    print(type(lista_productos))     # <class 'list'>  → es una lista
    print(type(lista_productos[0]))  # <class 'str'>   → el primer elemento es texto

    DIFERENCIA:
    - type(lista_productos)    pregunta: "¿qué tipo de objeto es la lista completa?"
    - type(lista_productos[0]) pregunta: "¿qué tipo de dato tiene el primer elemento?"
"""

# ==============================================================================
# ARCHIVO 13 — 13_actividad_2_listas.py
# TEMA: ANÁLISIS DE TEMPERATURAS SEMANALES
# ==============================================================================
"""
OBJETIVO DEL EJERCICIO:
    Practicar indexación positiva y negativa, slicing (rebanado de listas),
    y cálculo de promedios sobre fragmentos de una lista.

─────────────────────────────────────────────────────────────────────────────
PASO 1 — LISTA DE TEMPERATURAS (14 DÍAS)
─────────────────────────────────────────────────────────────────────────────
    temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]
    #  índice:       0   1   2   3   4   5   6   7   8   9  10  11  12  13

─────────────────────────────────────────────────────────────────────────────
PASO 2 — INDEXACIÓN POSITIVA Y NEGATIVA
─────────────────────────────────────────────────────────────────────────────
    temperaturas[0]   →  18  (primer día)
    temperaturas[-1]  →  19  (último día, índice negativo)
    temperaturas[6]   →  17  (día 7, recuerda que el índice empieza en 0)
    temperaturas[-2]  →  22  (penúltimo día)

    REGLA: Los índices NEGATIVOS cuentan desde el final de la lista.
           -1 es el último, -2 el penúltimo, etc.

─────────────────────────────────────────────────────────────────────────────
PASO 3 — SLICING (REBANADO DE LISTAS)
─────────────────────────────────────────────────────────────────────────────
    SINTAXIS: lista[inicio : fin : paso]
      - inicio: índice donde empieza el corte (incluido)
      - fin:    índice donde termina el corte (NO incluido)
      - paso:   de cuánto en cuánto avanza (opcional)

    EJEMPLOS DEL EJERCICIO:
        temperaturas[0:7:2]  →  Días 0, 2, 4, 6  (primera semana, cada 2 días)
        temperaturas[7:14:2] →  Días 7, 9, 11, 13 (segunda semana, cada 2 días)
        temperaturas[1::2]   →  Días 1, 3, 5, ... (días pares: índices impares)
        temperaturas[::-1]   →  Lista completa al revés

─────────────────────────────────────────────────────────────────────────────
PASO 4 — CALCULAR PROMEDIOS CON sum() Y len()
─────────────────────────────────────────────────────────────────────────────
    promedio = sum(lista) / len(lista)

    EJEMPLO:
        promedio_primera_semana = sum(temperaturas[0:7:2]) / len(temperaturas[0:7:2])
        promedio_segunda_semana = sum(temperaturas[7:14:2]) / len(temperaturas[7:14:2])

    ► sum()  →  Suma todos los valores de la lista.
    ► len()  →  Cuenta cuántos valores hay.
    ► Al dividir suma / cantidad, obtenemos el promedio.
    ► El :.2f en el f-string muestra solo 2 decimales.

─────────────────────────────────────────────────────────────────────────────
PASO 5 — BONUS: COMPARAR PROMEDIOS CON if / elif / else
─────────────────────────────────────────────────────────────────────────────
    if promedio_primera_semana > promedio_segunda_semana:
        print("La primera semana tuvo una temperatura promedio mayor.")
    elif promedio_segunda_semana > promedio_primera_semana:
        print("La segunda semana tuvo una temperatura promedio mayor.")
    else:
        print("Ambas semanas tuvieron la misma temperatura promedio.")

    ► Se comparan los dos promedios con operadores relacionales (>, <, ==).
    ► Dependiendo del resultado, se muestra un mensaje diferente.
"""

# ==============================================================================
# ARCHIVO 14 — 14_actividad_3_listas.py
# TEMA: GESTIÓN DE UNA LISTA DE REPRODUCCIÓN MUSICAL
# ==============================================================================
"""
OBJETIVO DEL EJERCICIO:
    Aplicar los métodos de modificación de listas (append, insert, extend,
    remove, pop, sort) sobre una playlist musical y responder preguntas
    usando métodos de consulta (len, index, count).

─────────────────────────────────────────────────────────────────────────────
PASO 1 — DECLARAR LA PLAYLIST INICIAL
─────────────────────────────────────────────────────────────────────────────
    canciones = ["cuatro babys,", "mala fama", "la jeepeta", "safaera", "yo perreo sola"]
    print(canciones)

    ► Se parte con 5 canciones ya definidas en la lista.

─────────────────────────────────────────────────────────────────────────────
PASO 2 — .append() → AGREGAR AL FINAL
─────────────────────────────────────────────────────────────────────────────
    canciones.append("tusa")
    print(canciones)

    ► "tusa" se agrega como último elemento de la lista.
    ► La lista ahora tiene 6 canciones.

─────────────────────────────────────────────────────────────────────────────
PASO 3 — .insert() → INSERTAR EN POSICIÓN ESPECÍFICA
─────────────────────────────────────────────────────────────────────────────
    canciones.insert(1, "callaita")
    print(canciones)

    ► "callaita" se inserta en la posición 1 (segunda posición).
    ► Los demás elementos se desplazan una posición hacia la derecha.
    ► La lista ahora tiene 7 canciones.

─────────────────────────────────────────────────────────────────────────────
PASO 4 — .extend() → FUSIONAR CON OTRA LISTA
─────────────────────────────────────────────────────────────────────────────
    canciones.extend(["Bonus Track 1", "Bonus Track 2"])
    print(canciones)

    ► extend() agrega TODOS los elementos de otra lista al final.
    ► Diferencia con append(): append() agregaría la lista como un solo elemento,
      extend() la "fusiona" elemento por elemento.
    ► La lista ahora tiene 9 canciones.

─────────────────────────────────────────────────────────────────────────────
PASO 5 — .remove() → ELIMINAR POR NOMBRE
─────────────────────────────────────────────────────────────────────────────
    canciones.remove("mala fama")
    print(canciones)

    ► Elimina la PRIMERA ocurrencia del elemento indicado.
    ► Si el elemento no existe, Python lanza un ValueError.
    ► La lista ahora tiene 8 canciones.

─────────────────────────────────────────────────────────────────────────────
PASO 6 — .pop() → ELIMINAR ÚLTIMO Y GUARDAR EL VALOR
─────────────────────────────────────────────────────────────────────────────
    ultima_cancion = canciones.pop()
    print(f"la ultima cancion eliminada es: {ultima_cancion}")
    print(canciones)

    ► pop() sin argumentos elimina y RETORNA el último elemento.
    ► El valor eliminado se guarda en la variable 'ultima_cancion'.
    ► La lista ahora tiene 7 canciones.

─────────────────────────────────────────────────────────────────────────────
PASO 7 — .sort() → ORDENAR ALFABÉTICAMENTE
─────────────────────────────────────────────────────────────────────────────
    canciones.sort()
    print(canciones)

    ► Ordena la lista de forma alfabética (A → Z).
    ► Modifica la lista ORIGINAL (no crea una nueva).
    ► Las mayúsculas tienen prioridad sobre las minúsculas en el orden ASCII.

─────────────────────────────────────────────────────────────────────────────
PASO 8 — CONSULTAS FINALES CON len(), .index() Y .count()
─────────────────────────────────────────────────────────────────────────────
    # ¿Cuántas canciones tiene la playlist?
    cantidad_canciones = len(canciones)
    print(f"la cantidad de canciones en la playlist es: {cantidad_canciones}")

    # ¿En qué posición está "cuatro babys,"?
    posicion_cuatro_babys = canciones.index("cuatro babys,")
    print(f"la posicion de la cancion cuatro babys es: {posicion_cuatro_babys}")

    # ¿Cuántas veces aparece "Bonus Track 1"?
    cantidad_bonus_track_1 = canciones.count("Bonus Track 1")
    print(f"la cantidad de veces que aparece Bonus Track 1 es: {cantidad_bonus_track_1}")

    MÉTODOS USADOS:
    ► len(lista)         →  Número total de elementos.
    ► lista.index(valor) →  Posición (índice) de un elemento.
    ► lista.count(valor) →  Cuántas veces aparece un elemento.
"""

# ==============================================================================
# RESUMEN GENERAL — MÉTODOS DE LISTAS EN PYTHON
# ==============================================================================
"""
╔══════════════╦═══════════════════════════════════════════════════════════╗
║ MÉTODO       ║ DESCRIPCIÓN                                               ║
╠══════════════╬═══════════════════════════════════════════════════════════╣
║ .append()    ║ Agrega un elemento al final de la lista                   ║
║ .insert()    ║ Inserta un elemento en una posición específica            ║
║ .extend()    ║ Fusiona otra lista al final                               ║
║ .remove()    ║ Elimina la primera ocurrencia de un valor                 ║
║ .pop()       ║ Elimina y retorna el último elemento (o por índice)       ║
║ .sort()      ║ Ordena la lista en orden ascendente / alfabético          ║
║ .reverse()   ║ Invierte el orden de la lista                             ║
║ .copy()      ║ Crea una copia independiente de la lista                  ║
║ .index()     ║ Devuelve el índice de un elemento                         ║
║ .count()     ║ Cuenta cuántas veces aparece un valor                     ║
║ len()        ║ Devuelve la cantidad de elementos de la lista             ║
║ sum()        ║ Suma todos los valores numéricos de la lista              ║
║ in           ║ Operador: verifica si un elemento existe en la lista      ║
╚══════════════╩═══════════════════════════════════════════════════════════╝

SLICING — REBANADO DE LISTAS
    lista[inicio:fin:paso]
    ► lista[0:7]    → Del índice 0 al 6
    ► lista[::2]    → Cada 2 elementos
    ► lista[::-1]   → Lista al revés

INDEXACIÓN
    ► Positiva: lista[0] → primer elemento
    ► Negativa:  lista[-1] → último elemento
"""

# FIN DEL DOCUMENTO
print("Documento explicativo de Listas en Python cargado correctamente.")
print("Archivos cubiertos: 11_Listas.py | 12_actividad_1_listas.py | 13_actividad_2_listas.py | 14_actividad_3_listas.py")
