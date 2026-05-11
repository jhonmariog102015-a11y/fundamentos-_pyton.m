# ============================================================
#  10: Ejercicios Prácticos de Python
# ============================================================
# Este archivo contiene 10 ejercicios que cubren los temas
# fundamentales de Python:
#   • Variables y tipos de datos (str, int, float, bool)
#   • Entrada de datos con input()
#   • Operadores aritméticos y de comparación
#   • Condicionales (if, elif, else)
#   • Bucles (for)
#   • Funciones matemáticas (math.sqrt, **)
#   • Intercambio de variables
#   • Operadores lógicos (booleanos)
#   • Cálculo de áreas y perímetros
#
# NOTA: Los ejercicios 2, 5 y 10 requieren entrada del
# usuario con input(), por lo que el programa se detendrá
# esperando datos del teclado.
# ============================================================

import math  # Se importa al inicio del archivo (buena práctica)


# ============================================================
#   EJERCICIO 1: Variables y print() básico
# ============================================================
# Qué hace:
#   Declara tres variables de distinto tipo (str, int, float)
#   y las muestra en una sola línea con print().
#
# Cómo funciona:
#   - nombre  → tipo str   (cadena de texto)
#   - producto → tipo int   (número entero, representa un precio)
#   - promedio → tipo float (número decimal)
#   - print() recibe varios argumentos separados por coma
#     y los une con un espacio automáticamente.
#
# Conceptos: variables, tipos de datos, print() con múltiples
#            argumentos8
# ============================================================

nombre = "pepito"
producto = 20000
promedio = 8.5

print("Mi nombre es", nombre, "y compraré un producto que vale",
      producto, "y tengo un promedio de", promedio)


# ============================================================
#   EJERCICIO 2: Lectura de datos, operaciones y condicionales
# ============================================================
# Qué hace:
#   Lee dos enteros y un float desde el teclado, calcula su
#   suma, determina cuál entero es mayor, divide el float
#   entre el resto de los enteros, y concatena dos cadenas.
#
# Cómo funciona:
#   - input() lee texto del teclado (siempre devuelve str).
#   - int() y float() convierten ese texto a número.
#   - Se usa if/elif/else para comparar los enteros.
#   - El operador % (módulo) obtiene el resto de la división.
#   - Se valida que no haya división entre cero.
#   - El operador + entre cadenas las concatena (une).
#
# Conceptos: input(), conversión de tipos, if/elif/else,
#            operadores aritméticos, concatenación de strings
# ============================================================

# Lectura de datos
entero1 = int(input("Ingrese el primer entero: "))
entero2 = int(input("Ingrese el segundo entero: "))
numero_float = float(input("Ingrese un número float: "))

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

# Suma de los tres números
suma = entero1 + entero2 + numero_float
print("\nLa suma de los tres números es:", suma)

# Mostrar el entero mayor
if entero1 > entero2:
    print("El entero mayor es:", entero1)
elif entero2 > entero1:
    print("El entero mayor es:", entero2)
else:
    print("Los dos enteros son iguales")

# División del float con el resto de la división de los enteros
if entero2 == 0:
    print("No se puede calcular el resto porque el segundo entero es 0")
else:
    resto = entero1 % entero2
    if resto != 0:
        resultado = numero_float / resto
        print("Resultado de la división:", resultado)
    else:
        print("No se puede dividir entre 0 porque el resto es 0")

# Concatenación de cadenas
concatenacion = cadena1 + " " + cadena2
print("Concatenación de cadenas:", concatenacion)


# ============================================================
#   EJERCICIO 3: Potenciación con el operador **
# ============================================================
# Qué hace:
#   Calcula la potencia de un número (base elevada al
#   exponente) usando el operador ** de Python.
#
# Cómo funciona:
#   - base ** exponente → equivale a base^exponente
#   - Ejemplo: 5 ** 3 = 5 × 5 × 5 = 125
#   - Se usa un f-string (f"...{variable}...") para insertar
#     variables directamente dentro del texto.
#
# Conceptos: operador de potencia (**), f-strings
# ============================================================

base = 5
exponente = 3
resultado = base ** exponente

print(f"El resultado de {base} elevado a la {exponente} es: {resultado}")


# ============================================================
#   EJERCICIO 4: Raíz cuadrada con math.sqrt() y bucle for
# ============================================================
# Qué hace:
#   Recorre una lista de números y calcula la raíz cuadrada
#   de cada uno usando la función math.sqrt().
#
# Cómo funciona:
#   - Se importa el módulo math (al inicio del archivo).
#   - Se crea una lista con varios números.
#   - El bucle for recorre cada elemento de la lista.
#   - math.sqrt(x) devuelve la raíz cuadrada de x.
#   - Se muestra el resultado con un f-string.
#
# Conceptos: módulo math, listas, bucle for, math.sqrt()
# ============================================================

numeros = [2, 8, 9, 27, 28, 55, 121]

for numero in numeros:
    raiz = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es: {raiz}")


# ============================================================
#   EJERCICIO 5: Promedio de notas de un estudiante
# ============================================================
# Qué hace:
#   Solicita el nombre de un estudiante y sus 5 notas,
#   calcula el promedio aritmético y muestra el resultado.
#
# Cómo funciona:
#   - input() lee el nombre como texto (str).
#   - float(input(...)) lee cada nota y la convierte a decimal.
#   - El promedio se calcula sumando las 5 notas y dividiendo
#     entre 5: promedio = (n1 + n2 + n3 + n4 + n5) / 5
#   - Se muestra el nombre y el promedio final.
#
# Conceptos: input(), float(), operaciones aritméticas, promedio
# ============================================================

nombre = input("Ingrese el nombre del estudiante: ")

nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))
nota5 = float(input("Ingrese la nota 5: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("\nNombre del estudiante:", nombre)
print("Promedio final:", promedio)


# ============================================================
#   EJERCICIO 6: Intercambio de valores entre variables
# ============================================================
# Qué hace:
#   Intercambia los valores de dos variables usando una
#   variable auxiliar (técnica clásica de programación).
#
# Cómo funciona:
#   1. Se guardan dos números en numeroUno y numeroDos.
#   2. Se copia el valor de numeroUno en auxiliar.
#   3. Se asigna el valor de numeroDos a numeroUno.
#   4. Se asigna el valor de auxiliar a numeroDos.
#   Resultado: los valores quedan intercambiados.
#
# Conceptos: asignación de variables, variable auxiliar (swap)
# ============================================================

numeroUno = 8
numeroDos = 2

print("Valores originales:")
print("numeroUno =", numeroUno)
print("numeroDos =", numeroDos)

auxiliar = numeroUno
numeroUno = numeroDos
numeroDos = auxiliar

print("\nValores intercambiados:")
print("numeroUno =", numeroUno)
print("numeroDos =", numeroDos)


# ============================================================
#   EJERCICIO 7: Operadores lógicos y tipo booleano
# ============================================================
# Qué hace:
#   Evalúa una expresión lógica compuesta usando el operador
#   'or' y muestra el resultado booleano (True o False).
#
# Cómo funciona:
#   - (5 == 2) → False  (5 no es igual a 2)
#   - (2 > 1)  → True   (2 sí es mayor que 1)
#   - False or True → True
#   - El operador 'or' devuelve True si AL MENOS UNA
#     de las condiciones es verdadera.
#
# Conceptos: operadores de comparación (==, >),
#            operador lógico (or), tipo bool
# ============================================================

estado = (5 == 2) or (2 > 1)

print("El valor de estado es:", estado)


# ============================================================
#   EJERCICIO 8: Operación aritmética combinada
# ============================================================
# Qué hace:
#   Evalúa una expresión aritmética compleja que combina
#   suma, resta, multiplicación, división, módulo y potencia.
#
# Cómo funciona:
#   Python respeta la precedencia de operadores (PEMDAS):
#     1. Paréntesis ()     → se evalúan primero
#     2. Exponentes **     → 2**2 = 4
#     3. *, /, %           → multiplicación, división, módulo
#     4. +, -              → suma, resta
#
#   Desglose paso a paso:
#     (15 + 5) = 20  →  20 * 2 = 40  →  40 / 4 = 10.0
#     (8 % 3) = 2    →  2 * 6 = 12
#     2**2 = 4
#     Resultado: 10.0 - 3 + 12 - 4 = 15.0
#
# Conceptos: precedencia de operadores, operadores aritméticos
# ============================================================

resultado = (15 + 5) * 2 / 4 - 3 + (8 % 3) * 6 - 2**2

print("El resultado de la operación es:", resultado)


# ============================================================
#   EJERCICIO 9: Área y perímetro de figuras geométricas
# ============================================================
# Qué hace:
#   Calcula el área y el perímetro de tres figuras:
#   cuadrado, triángulo y rectángulo.
#
# Cómo funciona:
#   CUADRADO (lado = 8):
#     Área      = lado × lado          = 8 × 8   = 64
#     Perímetro = 4 × lado             = 4 × 8   = 32
#
#   TRIÁNGULO (base=9, altura=8, lados=8,8):
#     Área      = (base × altura) / 2  = (9×8)/2 = 36
#     Perímetro = suma de los 3 lados  = 9+8+8   = 25
#
#   RECTÁNGULO (base=8, altura=6):
#     Área      = base × altura        = 8 × 6   = 48
#     Perímetro = 2 × (base + altura)  = 2×14    = 28
#
# Conceptos: fórmulas geométricas, operadores aritméticos
# ============================================================

# --- CUADRADO ---
ladoCuadrado = 8

areaCuadrado = ladoCuadrado * ladoCuadrado
perimetroCuadrado = 4 * ladoCuadrado

print("CUADRADO")
print("Área:", areaCuadrado)
print("Perímetro:", perimetroCuadrado)

# --- TRIÁNGULO ---
baseTriangulo = 9
alturaTriangulo = 8
ladoUnoTriangulo = 8
ladoDosTriangulo = 8

areaTriangulo = (baseTriangulo * alturaTriangulo) / 2
perimetroTriangulo = baseTriangulo + ladoUnoTriangulo + ladoDosTriangulo

print("\nTRIÁNGULO")
print("Área:", areaTriangulo)
print("Perímetro:", perimetroTriangulo)

# --- RECTÁNGULO ---
baseRectangulo = 8
alturaRectangulo = 6

areaRectangulo = baseRectangulo * alturaRectangulo
perimetroRectangulo = 2 * (baseRectangulo + alturaRectangulo)

print("\nRECTÁNGULO")
print("Área:", areaRectangulo)
print("Perímetro:", perimetroRectangulo)


# ============================================================
#   EJERCICIO 10: Clasificación por edad con condicionales
# ============================================================
# Qué hace:
#   Solicita la edad de una persona y la clasifica en una
#   categoría según el rango en el que se encuentre.
#
# Cómo funciona:
#   - Se lee la edad con input() y se convierte a int.
#   - Se usa una cadena de if/elif/else para determinar
#     en qué rango cae la edad:
#       0-5   → Infante         16-18 → Adolescente
#       6-10  → Niño            19-25 → Pre adulto
#       11-15 → Pre adolescente 26-40 → Adulto
#       41-55 → Pre anciano     56+   → Anciano
#   - Si la edad es negativa → "Edad no válida"
#
# Conceptos: if/elif/else, comparaciones encadenadas (a <= x <= b)
# ============================================================

edad = int(input("Ingrese la edad de la persona: "))

if 0 <= edad <= 5:
    categoria = "Infante"
elif 6 <= edad <= 10:
    categoria = "Niño"
elif 11 <= edad <= 15:
    categoria = "Pre adolescente"
elif 16 <= edad <= 18:
    categoria = "Adolescente"
elif 19 <= edad <= 25:
    categoria = "Pre adulto"
elif 26 <= edad <= 40:
    categoria = "Adulto"
elif 41 <= edad <= 55:
    categoria = "Pre anciano"
elif edad >= 56:
    categoria = "Anciano"
else:
    categoria = "Edad no válida"

print("La categoría de la persona es:", categoria)