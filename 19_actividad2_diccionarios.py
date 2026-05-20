  # ============================================================
#   ARCHIVO 19: Actividad Práctica de Diccionarios
# ============================================================
# En este ejercicio se simula una base de datos de alumnos.
# Se implementa la lógica para: calcular promedios de notas,
# generar reportes de aprobación y ordenar los datos de
# forma descendente según el rendimiento académico.
# ============================================================
# 1. Construcción del diccionario grupo
grupo = {
    101: {"nombre": "Juan Pérez", "edad": 18, "notas": [4.5, 3.8, 4.0, 5.0], "ciudad": "Medellín"},
    102: {"nombre": "Maria Lopez", "edad": 22, "notas": [3.0, 2.8, 3.5, 2.5], "ciudad": "Bogotá"},
    103: {"nombre": "Carlos Ruiz", "edad": 20, "notas": [5.0, 4.9, 4.8, 5.0], "ciudad": "Cali"},
    104: {"nombre": "Ana Gomez", "edad": 19, "notas": [2.5, 3.0, 2.0, 3.2], "ciudad": "Pereira"}
}

# 2. Fórmula para calcular promedio
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# 3. Impresión del reporte
print("-" * 60)
print(f"{'FICHA':<10} {'NOMBRE':<15} {'EDAD':<5} {'PROMEDIO':<10} {'ESTADO'}")
print("-" * 60)

for ficha, datos in grupo.items():
    promedio = calcular_promedio(datos['notas'])
    estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
    print(f"{ficha:<10} {datos['nombre']:<15} {datos['edad']:<5} {promedio:<10.2f} {estado}")

# 4. Agregar nuevo aprendiz y actualizar ciudad
grupo[105] = {
    "nombre": "Luis Torres", 
    "edad": 21, 
    "notas": [4.0, 4.2, 3.9, 4.1], 
    "ciudad": "Bucaramanga"
}

# Actualizar ciudad de la ficha 102
grupo[102]['ciudad'] = 'Cartagena'
print(f"\nCiudad de Maria actualizada a: {grupo[102]['ciudad']}")

# 5. Bonus: Lista ordenada de mayor a menor promedio
print("\n--- Aprendices ordenados por promedio (Mayor a Menor) ---")

aprendices_ordenados = sorted(
    grupo.items(), 
    key=lambda item: calcular_promedio(item[1]['notas']), 
    reverse=True
)

for ficha, datos in aprendices_ordenados:
    prom = calcular_promedio(datos['notas'])
    print(f"{datos['nombre']}: {prom:.2f}")
