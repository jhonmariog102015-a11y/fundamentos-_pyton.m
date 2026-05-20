# Guía Explicativa de Ejercicios de Python - Carpeta Fundame

Este documento proporciona una explicación detallada de la lógica y los conceptos aplicados en los ejercicios recientemente desarrollados y corregidos.

---

## 1. Gestión de Datos con Diccionarios
**Archivos:** `17_diccionarios.py` y `19_actividad2_diccionarios.py`

*   **Concepto:** Los diccionarios permiten almacenar datos en pares de `llave: valor`.
*   **Lógica Avanzada (`Actividad 2`):** 
    *   Se utilizan **diccionarios anidados** para representar una base de datos de aprendices, donde cada ficha (ID) contiene otro diccionario con detalles (nombre, notas, ciudad).
    *   **Cálculo de Promedios:** Se itera sobre las listas de notas usando `sum()` y `len()`.
    *   **Ordenamiento Personalizado:** Se utiliza la función `sorted()` junto con una expresión `lambda` para ordenar el diccionario de mayor a menor promedio sin perder la relación con las llaves originales (el ID de la ficha).

## 2. Operaciones Lógicas con Conjuntos (Sets)
**Archivo:** `20_actividad4_set.py`

*   **Concepto:** Los conjuntos son colecciones de elementos únicos, ideales para comparar listas de inscritos y eliminar duplicados.
*   **Operaciones Aplicadas:**
    *   **Unión (`|`):** Para obtener el total de estudiantes sin repeticiones.
    *   **Intersección (`&`):** Para encontrar quiénes comparten varios cursos.
    *   **Diferencia (`-`):** Para identificar quiénes pertenecen exclusivamente a un grupo.
    *   **Lógica de "Exactamente Dos":** Se calcula uniendo las intersecciones de cada par de cursos y restando a los que están en los tres, logrando un filtrado preciso.

## 3. Lógica de Control y Manejo de Errores
**Archivos:** `07_medidor_imc.py` y `08_juego_adivinanza.py`

*   **Bucles Infinitos Controlados:** Se usa `while True` con una condición de salida (`break`) basada en la respuesta del usuario (`si/no`), permitiendo repetir el cálculo o el juego sin reiniciar el script.
*   **Robustez (`Try/Except`):** En el juego de adivinanza, se implementó un bloque `try-except` para capturar errores. Si el usuario ingresa una letra en lugar de un número, el programa no se detiene ("crush"), sino que pide el dato correctamente.

## 4. Fundamentos y Geometría
**Archivo:** `10_ejercicios_practicos.py`

*   **Precedencia de Operadores:** El ejercicio 8 demuestra cómo Python evalúa expresiones matemáticas complejas siguiendo el orden de importancia (Paréntesis, Exponentes, Multiplicación/División, Suma/Resta).
*   **Cálculos Geométricos:** Aplicación de fórmulas estándar para áreas y perímetros de figuras (cuadrado, triángulo, rectángulo) usando operadores aritméticos.

## 5. Manipulación de Listas y Slicing
**Archivos:** `13_actividad_2_listas.py` y `14_actividad_3_listas.py`

*   **Slicing (Rebanado):** Uso de la sintaxis `[inicio:fin:paso]` para extraer sub-listas (por ejemplo, obtener temperaturas de días específicos o invertir el orden de una lista completa).
*   **Métodos Dinámicos:** Gestión de una playlist musical utilizando `.append()`, `.insert()`, `.extend()`, `.remove()` y `.pop()` para modificar el contenido de forma estructurada.

---
*Documento generado para facilitar la revisión técnica y el estudio de los fundamentos de programación en Python.*